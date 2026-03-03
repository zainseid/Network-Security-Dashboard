from flask import Flask, jsonify
from flask_cors import CORS
from ldap3 import Server, Connection, ALL
import config

app = Flask(__name__)
CORS(app)

def get_ad_users():
    try:
        c = config.AD_CONFIG
        server = Server(c['SERVER'], get_info=ALL)
        conn = Connection(server, user=c['ADMIN'], password=c['PASSWORD'], auto_bind=True)
        
        # جلب سمات المستخدمين بما فيها عدد محاولات الدخول الخاطئة
        conn.search(c['BASE_DN'], '(&(objectCategory=person)(objectClass=user))', 
                    attributes=['displayName', 'sAMAccountName', 'distinguishedName', 'whenCreated', 'badPwdCount'])
        
        users = []
        # أنماط حقن SQL المشبوهة
        sql_payloads = ["'", "--", ";", "DROP", "SELECT", "OR 1=1"]
        
        for e in conn.entries:
            username = str(e.sAMAccountName)
            display_name = str(e.displayName) or username
            
            # الحل الجذري لخطأ المقارنة: تحويل القيمة إلى int بشكل آمن
            bad_attempts = int(e.badPwdCount.value) if (hasattr(e, 'badPwdCount') and e.badPwdCount.value) else 0
            
            # فحص محاولات SQL Injection
            is_sql = any(p in username.upper() or p in display_name.upper() for p in sql_payloads)
            
            # تحديد نوع التهديد
            threat_type = "Clean"
            if is_sql:
                threat_type = "SQL Injection Attempt"
            elif bad_attempts > 0:
                threat_type = f"Brute Force ({bad_attempts} failed attempts)"

            users.append({
                "name": display_name,
                "username": username,
                "ou": next((p.replace('OU=', '') for p in str(e.distinguishedName).split(',') if p.startswith('OU=')), 'Users'),
                "created_at": e.whenCreated.value.strftime('%Y-%m-%d %H:%M') if e.whenCreated else "N/A",
                "is_threat": bad_attempts > 0 or is_sql,
                "threat_type": threat_type
            })
            
        conn.unbind()
        return users
    except Exception as e:
        print(f"CRITICAL ERROR: {e}") # سيظهر في الـ Terminal لتسهيل التتبع
        return []

@app.route('/ad-data')
def api_data():
    users = get_ad_users()
    return jsonify({"users": users})

# مسار جديد خاص بالتحليل لضمان عمل Data Analysis
@app.route('/ad-analysis')
def ad_analysis():
    users = get_ad_users()
    total = len(users)
    threats = [u for u in users if u['is_threat']]
    
    ou_counts = {}
    for u in users:
        ou_counts[u['ou']] = ou_counts.get(u['ou'], 0) + 1

    return jsonify({
        "total_users": total,
        "threat_count": len(threats),
        "sql_threats": len([u for u in threats if "SQL" in u['threat_type']]),
        "health_score": round(((total - len(threats)) / total * 100), 1) if total > 0 else 0,
        "ou_data": ou_counts
    })

if __name__ == '__main__':
    # تحذير: هذا سيرفر تطوير، لا تستخدمه في الإنتاج الحقيقي
    app.run(host='0.0.0.0', port=5000, debug=True)
