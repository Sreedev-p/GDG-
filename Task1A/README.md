# GDG Recruitments 2026: Cybersecurity Task 1
**Candidate:** [Sreedev P]
**Focus:** Forensics, Reverse Engineering & Automation

---

## 📁 Task 1A: The Multi-Part Forensics Challenge
**Objective:** Assemble a three-part flag in the format: `Gdg{part1_part2_part3}`.

### Part 1: Git Forensics
* **Method:** Found a hidden git directory and investigated rewritten history using `git reflog` to find "lost" commits.
* **Discovery:** Identified a suspicious commit hash with the message: `"(oops, committed secrets!)"`.
* **Action:** Used `git checkout [commit_hash]` to recover a hidden configuration file from that point in time.
* **Fragment 1:** `+FLAG_PART_1=gdg{sw1ss_`



### Part 2: Image Forensics (Steganography)
* **Method:** Analyzed the file `heheheha.png` using `binwalk`.
* **Discovery:** Found an embedded Zlib compressed stream at offset `29`.
* **Action:** Extracted data using `binwalk -e`. Due to header corruption, I used the `strings` utility to pull human-readable text directly from the binary blob. There were multiple string of same format and got the following flag in the string list
* **Command:** `strings _heheheha.png.extracted/29.zlib | grep "_"`
* **Fragment 2:** `aLs9aA_`



### Part 3: QR Code Mass-Automation
* **Method:** Analyzed a directory containing 3,000 unique QR code images.
* **Action:** Developed a Bash script to automate the scanning process using `zbarimg`.
* **Process:** Piped results into `scanreport.txt`, used `grep -v` to filter out unwanted results, and decoded the resulting Base64 string using the `base64` utility.
* **Automation Script (`scan.sh`):**
    ```bash
    #!/bin/bash
    echo "Starting scan..."
    for file in *.png; do
        zbarimg "$file" >> scanreport.txt
    done
    ```
* **Fragment 3:** `part3=gg1ol}`



