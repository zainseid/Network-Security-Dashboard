# 🛡️ Hybrid Automated Threat Response System (SOC Automation)

This project demonstrates a full-cycle Cyber Security Operation Center (SOC) automation. It detects SQL Injection attacks in real-time, visualizes them on a dashboard with timestamps, and executes automated mitigation on both Host (Linux) and Network (FortiGate) levels.

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
