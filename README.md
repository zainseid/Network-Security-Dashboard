# 🛡️ Hybrid Automated Threat Response System (SOC Automation)

"This system provides a full-loop defense mechanism. Initially, the attacker can ping the server. Once an SQLi attack is detected and timestamped by the Live Monitor, the Auto-Blocker executes an iptables drop and syncs with FortiGate. Post-mitigation, any ping from the attacker results in a Request Timeout."

## 🚀 System Architecture


1. **Detection Layer**: A Python Flask API (`network_api.py`) acts as a honeypot, capturing attack signatures and metadata (IP, Username, Timestamp).
2. **Visualization Layer**: A React-based Storybook dashboard provides live monitoring of blocked threats.
3. **Response Layer (Local)**: `block_ip.py` monitors the API and triggers `iptables` for immediate local host protection.
4. **Response Layer (Enterprise)**: `fortigate_block.py` uses the **FortiGate REST API** to push attacker IPs into the network-wide firewall address list.

## 🛠️ Technical Stack
- **Backend**: Python, Flask, REST API.
- **Frontend**: React, Storybook.
- **Security**: Linux Iptables, FortiOS API.
- **Data**: JSON-based real-time threat feed.

## 📸 Proof of Concept
### Real-Time Monitoring with Timestamps
The dashboard captures the exact moment of the attack:
- **Attacker IP**: 192.168.47.110
- **Status**: Blocked
- **Timestamp**: Included for forensic logging.

### Automated Mitigation
- **Local Firewall**: Successfully executed `DROP` command.
- **Network Firewall**: Successfully created Address Object in FortiGate via API (`Status 200 OK`).

## ⚙️ How to Run
1. Start the monitoring API: `python3 network_api.py`
2. Run the automated local blocker: `sudo python3 block_ip.py`
3. Execute the FortiGate sync: `python3 fortigate_block.py`
   
🛡️ How the SOC Automation Stack Works
This project implements a full-loop Security Operations Center (SOC) automation, from threat detection to network-wide isolation. The system is divided into three main layers:

1. Detection Layer (The Brain)
Real-time Monitoring: The Flask-based API (network_api.py) intercepts incoming requests and scans for malicious patterns like SQL Injection (' OR 1=1).

Contextual Logging: Upon detection, the system captures the attacker's metadata, including the precise Timestamp and Threat Type.

Instant Rejection: The API immediately blocks the local request with a 403 Forbidden status to protect the web application.

2. Visualization Layer (The Dashboard)
Live Monitoring: A React/Storybook frontend provides a high-visibility dashboard for security analysts.

Automated Updates: The dashboard polls the security API every 3 seconds to display the latest active threats.

Detailed Alerts: Each threat is displayed with its unique IP address, discovery time, and current enforcement status.

3. Enforcement Layer (The Shield)
Network Isolation: The backend triggers a script to communicate with the FortiGate Firewall via its REST API.

Dynamic Addressing: The system automatically creates a new Address Object specifically for the attacker's IP.

Top-Level Blocking: The IP is added to a high-priority DENY Policy (Block_Automated_Attacks), ensuring the attacker is completely isolated from the entire corporate network, including internal servers like Active Directory.
