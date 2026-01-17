# Task 1B: Reverse Engineering - apple_pie

## Challenge Overview
The target was a 32-bit ELF executable named 'apple_pie'. My objective was to bypass the password gate and extract the hidden flag.

## Tools Used
- file (File identification)
- chmod (Permission management)
- strings (Static analysis)
- nm (Symbol table analysis)
- ltrace (Library call interception)
- objdump (Disassembly)
- GDB (Dynamic hijacking)

## Step-by-Step Walkthrough

### 1. Preparation & Identification
Initial execution failed with "permission denied". I identified the file as a 32-bit ELF and granted execution rights.
- Command: `file apple_pie`
- Command: `chmod +x apple_pie`

### 2. Static Analysis
Running `strings` revealed several interesting clues:
- A clear-text password hint: `not_the_password`
- A success message template: `You found the hidden treasure: %s`
- Obfuscated data blocks: `bab~`, `U4@Z`, `6}ui`, etc.

Using `nm`, I discovered a "hidden" function that was not being called in the main execution flow:
- Function: `000011cd T def_nothing_important`

### 3. Dynamic Analysis (ltrace)
I used `ltrace` to monitor the password verification logic.
- Observation: The program used `strncmp` to check my input against "not_the_password".
- Observation: Even with the correct password, the program requested secondary input and then triggered a SIGSEGV (Segmentation Fault).

### 4. Reverse Engineering the Obfuscation
I disassembled the hidden function using `objdump`:
- Command: `objdump -d ./apple_pie`
- Finding: The function `def_nothing_important` manually loads hex values onto the stack and performs an `XOR 0x5` operation in a loop to decode the flag.

### 5. Dynamic Hijacking (The Solution)
To avoid manual decryption, I used GDB to force the CPU to execute the hidden function:
1. `gdb ./apple_pie`
2. `break main`
3. `run`
4. `call (void) def_nothing_important()`

## Result
The program bypassed the standard logic and printed the decrypted flag:
**gdg{P1E_3xpl01ted_lol}**
