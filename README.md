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
