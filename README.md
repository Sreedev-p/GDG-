# GDG Recruitments 2026: Cybersecurity Challenge
**Candidate:** Sreedev P
**Status:** 1st Year Student, VIT
**Focus:** Forensics, Reverse Engineering & Server Exploitation

---

## 📁 Task 1: Forensics & Reverse Engineering

### 1A: The Multi-Part Forensics Challenge
**Objective:** Reconstruct a three-part flag (`Gdg{part1_part2_part3}`) by investigating hidden data across different formats.

* **Part 1: Git Forensics**
    * **Method:** Investigated rewritten history using `git reflog` to identify lost commits.
    * **Discovery:** Located a commit hash for "(oops, committed secrets!)" and recovered a hidden configuration file containing the first fragment.
    * **Fragment:** `gdg{sw1ss_`
* **Part 2: Image Forensics (Steganography)**
    * **Method:** Analyzed `heheheha.png` with `binwalk -e` to extract a Zlib compressed stream at offset 29.
    * **Action:** Used `strings` on the resulting binary blob to bypass header corruption and filter the second fragment.
    * **Fragment:** `aLs9aA_`
* **Part 3: QR Code Mass-Automation**
    * **Method:** Developed a **Bash script** to automate the scanning of 3,000 unique QR code images using `zbarimg`.
    * **Process:** Piped results into a report, utilized `grep -v` to filter noise, and decoded the final Base64 string.
    * **Fragment:** `gg1ol}`

**Complete Flag:** `gdg{sw1ss_aLs9aA_gg1ol}`

### 1B: Reverse Engineering - "apple_pie"
**Objective:** Bypass the authentication gate of a 32-bit ELF executable.

* **Analysis:** Identified the file as a 32-bit ELF and used `strings` to find a cleartext password candidate: `not_the_password`.
* **Discovery:** Used `nm` to locate a hidden function `def_nothing_important` that performs an `XOR 0x5` decryption loop.
* **Solution (Dynamic Hijacking):** Utilized **GDB** to force-call the hidden function during runtime, successfully bypassing the standard logic and a secondary SIGSEGV (Segmentation Fault).
* **Final Flag:** `gdg{P1E_3xpl01ted_lol}`

---

## 📁 Task 2: Server Hacking - "The Hidden Recipe"
**Objective:** Network-wide reconnaissance, traffic interception, and server exploitation attempts.

### 1. Network Reconnaissance & Discovery
* **Environment:** Verified local network configuration with `ip -a`.
* **Host ID:** Performed an `nmap -sn` ping sweep to locate the target machine.
* **Service Scanning:** Executed `nmap -sV` to identify active services: **SSH (22)**, **HTTP (80/8080)**, and **FTP (21)**.

### 2. Enumeration & Credential Discovery
* **Directory Brute-forcing:** Used `gobuster` to find a `/logs` directory containing unsecured data repositories.
* **Log Analysis:** Extracted leaked credentials from a specific data field:
    * **User:** `deploy`
    * **Password:** `Spring2021!`

### 3. Exploitation & Interception
* **Traffic Analysis:** Utilized **Wireshark** to perform live packet capture on **FTP** and **HTTP** traffic to hunt for cleartext session tokens.
* **Authentication Bypass:**
    * Attempted to log in via **SSH** with the `deploy` credentials; access was restricted.
    * Attempted **Cookie Manipulation** by manually setting `admin=true` to force administrative access.
    * Analyzed the **Node.js** backend for environment-specific vulnerabilities and logic bypasses.
* **Data Filtering:** Used `grep -v` (inverse matching) to strip out system noise and "permission denied" errors from scan reports to isolate potential flag strings.

---

## 🛠 Toolbelt Summary
| Category | Tools Used |
| :--- | :--- |
| **Network & Web** | Nmap, Gobuster, Wireshark |
| **Forensics** | Binwalk, Git Reflog, Strings, Zbarimg |
| **Reversing** | GDB, Ltrace, NM, Objdump, File |
| **Automation** | Bash Scripting, Grep (Inverse Matching) |

---

## 🏁 Conclusion
This challenge demonstrated my ability to apply systematic enumeration and automation to complex datasets. From GDB hijacking to protocol analysis in Wireshark, I maintained a "best effort" approach to identify and document every potential attack vector, ensuring a thorough technical assessment for the GDG recruitment process.
