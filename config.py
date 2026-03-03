# ==========================================================
# 🛡️ Global Security Lab Configuration
# ==========================================================

# config.py

# 🔌 Ports & API Settings
API_PORT = 5001

# 🖥️ Infrastructure IPs
FORTIGATE_IP = "192.168.47.1"
AD_SERVER_IP = "192.168.47.100"
INFOBLOX_IP  = "192.168.47.10"

# 📂 Active Directory Configuration Object
# هذا هو الجزء الذي يسبب الخطأ إذا كان ناقصاً
AD_CONFIG = {
    'SERVER': AD_SERVER_IP,
    'PORT': 389,
    'ADMIN': "administrator@fairdeal.local",
    'PASSWORD': "***************************",
    'BASE_DN': "DC=fairdeal,DC=local",
    'TOTAL_USERS': 14  # الرقم الذي سيظهر في الواجهة
}

# 🛡️ FortiGate & Infoblox Credentials
# config.py
FORTIGATE_CONFIG = {
    'IP': "192.168.47.1",
    'PORT': 8443,
    'ADMIN': "AI_Agent",
    'PASSWORD': "************************",
    'TOKEN': "***************************",  # الـ Token يغنيك عن اليوزر والباسورد في الأتمتة
    'POLICY_ID': 3             # رقم السياسة التي سنضيف لها الحظر
}
# --- 🌐 إعدادات الإنفوبلوكس (Infoblox Settings) ---
# تستخدم لجلب أحمال الشبكة (83% Load) التي تظهر في الواجهة
INFOBLOX_CONFIG = {
    'IP': "192.168.47.10",
    'PORT': 443,
    'ADMIN': "admin",
    'PASSWORD': "*********************************",
    'WAPI_VERSION': "v2.12"
}
# --- 🔌 إعدادات السيرفر العام ---
API_PORT = 5001
