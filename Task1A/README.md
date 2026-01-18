# GDG Recruitments 2026: Cybersecurity Task 1
**Candidate:** [Your Name]
**Focus:** Forensics & Reverse Engineering

---

## 📁 Task 1A: The Multi-Part Forensics Challenge
**Objective:** Assemble a three-part flag in the format: `Gdg{part1_part2_part3}`.

### Level 1: Git Forensics
* **Method:** Investigated rewritten history using `git reflog` to find "lost" commits.
* **Discovery:** Identified a suspicious commit labeled `"(oops, committed secrets!)"`.
* **Action:** Used `git checkout [commit_hash]` to recover a hidden config file.
* **Fragment 1:** `[Insert_Part_1_Here]`

### Level 2: Steganography & Image Analysis
* **Method:** Analyzed `heheheha.png` using `binwalk`.
* **Discovery:** Found an embedded Zlib stream at offset `29`. 
* **Action:** Extracted the data using `binwalk -e`. Due to header corruption, I used the `strings` utility to pull human-readable text directly from the binary blob.
* **Command:** `strings _heheheha.png.extracted/29.zlib | grep "_"`
* **Fragment 2:** `[Insert_Part_2_Here]`

### Level 3: Advanced Python Decompression
* **Method:** Handled a raw DEFLATE stream that failed standard Zlib checks.
* **Action:** Developed a Python script using `zlib.decompress(data, -15)` to bypass header requirements and extract the final text.
* **Fragment 3:** `[Insert_Part_3_Here]`

**Final Flag 1:** `Gdg{[Part1]_[Part2]_[Part3]}`

---

## 📁 Task 1B: Reverse Engineering - apple_pie
**Objective:** Bypass a broken password gate in an ELF 32-bit executable.

### 1. Initial Analysis & Permissions
Identified the file as a 32-bit ELF and updated execution permissions.
```bash
file apple_pie
chmod +x apple_pie
