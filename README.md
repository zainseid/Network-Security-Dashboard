🛡️ AI-Powered SOC Automation Stack: Real-Time Threat Detection & Network Isolation
Stop Attacks in Milliseconds, Not Minutes.
This project demonstrates a fully automated Security Operations Center (SOC) lifecycle, from zero-day threat detection to network-wide attacker isolation. By combining a custom-built threat detection API with the power of FortiGate Next-Generation Firewalls, this stack reduces the Mean Time to Respond (MTTR) from minutes to milliseconds, ensuring zero manual intervention.

🚀 Key Features
⚡ Zero-Latency Detection: Custom Flask-based API instantly identifies malicious patterns, including SQL Injection and other web attacks, directly at the application layer.

📊 Dynamic SOC Dashboard: A high-visibility, real-time interface built with React & Storybook, providing analysts with a live feed of active threats, attacker IPs, and precise timestamps.

🛡️ Automated FortiGate Integration: Seamlessly communicates with the FortiGate REST API to create on-the-fly Address Objects for identified attackers.

🚫 Network-Wide Enforcement: Automatically injects attacker IPs into a high-priority DENY Policy, instantly isolating them from the entire corporate infrastructure, including internal servers like Active Directory.

📖 How It Works: The Full SOC Lifecycle
This project implements a complete defense-in-depth strategy, divided into three powerful layers:

1. Detection Layer (The Brain)
The Flask security API (network_api.py) acts as a vigilant sentinel, intercepting all incoming requests and scanning them for attack signatures.

When a threat is detected, it is immediately logged with a unique Timestamp and Threat Type for full forensic accountability.

2. Visualization Layer (The Dashboard)
The Storybook dashboard provides a centralized "source of truth" for security events.

It visualizes attack data, transforming raw logs into actionable intelligence for immediate situational awareness.

3. Enforcement Layer (The Shield)
An automation script (block_ip.py) acts as the "hands" of the system, instantly pushing the attacker's details to the FortiGate Firewall.

A new Address Object is created, and a top-of-the-list DENY policy is applied. This ensures that any subsequent traffic from the attacker IP is dropped, effectively preventing lateral movement and data exfiltration.

🛠️ Technology Stack
Language: Python (Flask, Requests, Datetime)

Frontend: React, Storybook

Security: FortiGate Next-Generation Firewall (REST API)

Environment: Linux (Web Server), Kali Linux (Attacker), Active Directory Server (Internal)

📊 Visual Proof of Concept (PoC)
Here is the visual evidence of the system in action, from detection to enforcement.

1. Network Architecture & Attack Diagram
This diagram illustrates the logical flow of the system. The attacker on Kali Linux targets the Web Server. The attack is detected, and a blocking command is sent to the FortiGate, which then isolates the attacker from all internal devices.

2. Live Threat Detection Dashboard
This screenshot from Storybook shows the live "Active Threats" feed. Notice how each attack is logged with a precise IP address and Discovery Time, indicating that the backend is successfully generating and sending this data.

3. Automated FortiGate Address Object Creation
As soon as an attack is logged, the automation script creates a corresponding Address Object in FortiGate. This image confirms the creation of AI_BLOCK_192_168_47_110 with a full host mask (255.255.255.255), proving the REST API integration is successful.

4. Final Network Enforcement (The Block)
This is the ultimate proof of successful automation. The Block_Automated_Attacks policy, created via API, is now in the top-of-list position. The action is set to DENY, effectively isolating the attacker from all destinations within the network, including internal resources that were previously reachable.
