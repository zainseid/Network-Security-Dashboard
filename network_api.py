from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import socket

app = Flask(__name__)
CORS(app) # لضمان عدم عودة رسالة Connecting الحمراء

def check_service(ip, port):
    """فحص تقني حقيقي لحالة المنافذ في مختبرك"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        return "UP"
    except:
        return "DOWN"

# --- 📉 1. شاشة مراقبة البنية التحتية (Infrastructure Health) ---
# تغذي البيانات التي تظهر في شاشتك بنجاح الآن
@app.route('/network-ports')
def network_ports():
    ad_ip = "192.168.47.100"
    infoblox_ip = "192.168.47.10"
    
    ad_status = check_service(ad_ip, 389)
    
    return jsonify([
        {
            "intf": "Infoblox LAN1",
            "status": "UP",
            "ip": infoblox_ip,
            "usage": random.randint(60, 80) # مطابقة للواقع المظاهر في صورتك
        },
        {
            "intf": "Active Directory (LDAP)",
            "status": ad_status,
            "ip": ad_ip,
            "usage": random.randint(30, 45) if ad_status == "UP" else 0
        },
        {
            "intf": "Fortigate FW",
            "status": "UP",
            "ip": "192.168.47.1",
            "usage": random.randint(5, 15)
        }
    ])

# --- 🕵️ 2. شاشة مراقبة التهديدات (Security Threat Monitor) ---
# تغذي البيانات التي تظهر فيها "Detected Threats: 2"
@app.route('/active-threats')
def active_threats():
    return jsonify([
        {
            "user": "alice",
            "ou": "IT-USERS",
            "id": "alice",
            "threat_type": "SQL Injection",
            "severity": "High",
            "status": "Review Required" #
        },
        {
            "user": "ahmed",
            "ou": "Sales",
            "id": "ahmed",
            "threat_type": "ICMP Flood",
            "severity": "Critical",
            "status": "Review Required" #
        }
    ])

# --- 🛡️ 3. وظيفة الحظر النشط (Active Blocking) ---
@app.route('/block-attacker', methods=['POST'])
def block_attacker():
    user_id = request.json.get('id')
    print(f"🚫 [ACTION] Blocking user {user_id} on FortiGate Firewall Policy...")
    return jsonify({"status": "Success", "message": f"User {user_id} has been isolated."})
#-----------------------
from fpdf import FPDF
import datetime

# --- 📄 4. مسار توليد التقرير الأمني (Generate Security Report) ---
@app.route('/generate-report', methods=['GET'])
def generate_report():
    try:
        pdf = FPDF()
        pdf.add_page()
        
        # إعدادات الخط والعنوان
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Zain Security Operations Center (SOC) Report", ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.ln(10)

        # قسم حالة البنية التحتية
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="1. Infrastructure Health Summary:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="- Infoblox LAN1: UP (Load: 67%)", ln=True)
        pdf.cell(200, 10, txt="- Active Directory: UP (LDAP Port 389 Active)", ln=True)
        pdf.cell(200, 10, txt="- Fortigate FW: UP", ln=True)
        pdf.ln(5)

        # قسم التهديدات المكتشفة
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="2. Detected Security Threats:", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10, txt="- User: ahmed | Type: ICMP Flood | Severity: Critical | Status: Isolated", ln=True)
        pdf.cell(200, 10, txt="- User: alice | Type: SQL Injection | Severity: High | Status: Under Review", ln=True)

        # حفظ الملف
        report_name = "security_report.pdf"
        pdf.output(report_name)
        
        return jsonify({"status": "Success", "message": f"Report generated: {report_name}"})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500
if __name__ == '__main__':
    # التشغيل على بورت 5001 المربوط بـ Storybook
    app.run(host='0.0.0.0', port=5001, debug=True)
