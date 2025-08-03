# Log Analyzer – Python Tool for Detecting Suspicious Login Attempts

## 📌 Overview
This simple Python script scans system log files (like `auth.log`) to detect and print suspicious login attempts. It flags common signs of brute-force attacks such as "Failed password" and "authentication failure."

---

## 🧠 Skills Demonstrated
- Python scripting
- Log analysis
- String matching & filtering
- Terminal usage (Mac)
- Working with files and I/O

---

## 📂 Files
- `main.py` – the main script
- `sample.log` – a fake system log file with successful and failed login attempts

---

## 🔍 Sample Output

```bash
[!] Found 3 suspicious log entries:

Jul 26 15:00:00 server sshd[1234]: Failed password for invalid user root from 192.168.1.10 port 22 ssh2
Jul 26 15:01:01 server sshd[1234]: Failed password for user admin from 192.168.1.20 port 22 ssh2
Jul 26 15:03:12 server sshd[1234]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.40
python3 main.py
