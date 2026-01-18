# Task 2: Server Hacking - "The Hidden Recipe"
**Objective:** Network enumeration, traffic interception, and server exploitation attempts.

---

## 🔍 Phase 1: Network Reconnaissance & Discovery
The assessment began by verifying the local environment and identifying the target's presence on the network.

### 1. Environment & Host Identification
I started by verifying my own network interfaces using `ip -a`. Once confirmed, I performed a host discovery scan (Ping Sweep) to locate the active target machine within the network range.

**Commands used:**
* `ip -a`
* `nmap -sn <target_network_range>`

### 2. Service & Version Scanning
After locating the target IP, I performed an aggressive service scan to discover open ports and the specific versions of the software running.

**Command used:**
* `nmap -sV <target_ip>`

**Open Ports Identified:** SSH (22), HTTP (80/8080), and FTP (21).



---

## 🛠 Phase 2: Web Enumeration & Credential Discovery
I shifted focus to the web application to map hidden directories and search for sensitive data leaks.

### 1. Directory Brute-forcing
Using `gobuster`, I performed a directory search to find unlinked files and hidden folders.
* **Command:** `gobuster dir -u http://<target_ip> -w /usr/share/wordlists/dirb/common.txt`
* **Discovery:** This led to a `/logs` directory.

### 2. Log Analysis & Credential Extraction
Inside the logs, I discovered a data field that contained leaked credentials:
* **Username:** deploy
* **Password:** Spring2021!

---

## 🕵️ Phase 3: Traffic Interception & Exploit Attempts
With initial credentials and service info, I attempted to escalate access and intercept sensitive packets.

### 1. Protocol Interception (Wireshark)
I utilized **Wireshark** to perform live packet capture and deep packet inspection (DPI). I focused on intercepting **FTP** and **HTTP** packets to look for cleartext communications or re-usable session tokens.



### 2. Authentication & SSH Bypass Attempts
* **SSH Login Failure**: I attempted to log in via **SSH** using the `deploy` credentials and the password `Spring2021!`. Despite the credentials being valid, the connection was refused, suggesting the account was restricted or locked for remote access.
* **Cookie Manipulation**: On the web service, I intercepted the traffic and attempted to bypass authentication by manually setting the session cookie to `admin=true` to force administrative access.
* **Node.js Environment Analysis**: After identifying a **Node.js** backend, I researched environment-specific vulnerabilities and tested several Node-based exploitation techniques to bypass the application logic.


---

## 🏁 Conclusion
During this intensive assessment, I successfully mapped the target network, discovered leaked credentials via logs, and analyzed raw traffic via Wireshark. Although the final flag was not retrieved due to the high level of hardening on the Node.js server and restricted `deploy` account access, the systematic approach of enumeration, interception, and automated filtering represents a dedicated "best effort" approach to the challenge.

---

## 🚀 Tools Used
* **IP/Nmap**: Network mapping and service versioning.
* **Gobuster**: Web directory enumeration.
* **Wireshark**: FTP and HTTP packet interception.
* **SSH/FTP**: Remote access protocols.
