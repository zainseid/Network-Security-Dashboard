# 🛡️ ZAIN-SOC: AI-Driven Network Automation & Security Monitor

This project is a sophisticated Security Operations Center (SOC) Dashboard built with **React (Storybook)** and **Flask**. It features real-time monitoring and automated threat mitigation.

## 🚀 Key Features

* **Real-time Port Monitoring**: Live tracking of **Infoblox** and **Active Directory** status using socket-level checking.
* **Automated Threat Mitigation**: Detects **SQL Injection** and **ICMP Flood** attacks and automatically triggers block commands on **FortiGate Firewall**.
* **Dynamic Security Reports**: Generates professional PDF audit reports summarizing network health and blocked incidents.
* **Infrastructure Integration**: Full connectivity with:
    * **FortiGate** (API-based Blocking)
    * **Infoblox** (IPAM Tracking)
    * **Active Directory** (LDAP Status Monitoring)

## 🛠️ Tech Stack

* **Frontend**: React.js, Storybook
* **Backend**: Python Flask, Flask-CORS
* **Security Tools**: FortiGate API, FPDF (Reporting)

## 📸 Screenshots
- **Port Monitor**: Shows 83% Load on Infoblox and UP status for AD.
- **Threat Monitor**: Displays detected critical threats for users like `ahmed` and `alice`.

## ⚙️ Setup
1. Activate virtual environment: `source venv/bin/activate`
2. Install dependencies: `pip install flask flask-cors requests fpdf`
3. Run the API: `python3 network_api.py`
4. Start Storybook: `npm run storybook`
