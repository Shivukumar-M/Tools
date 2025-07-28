# 🔍 Python Port Scanner

A simple multi-threaded Python port scanner that checks for open TCP ports on one or multiple targets.  
It is lightweight, fast (due to threading), and easy to use.

---

## 🚀 Features
- Scan **single or multiple IP addresses**
- Specify **number of ports to scan** (from port 1 to N)
- **Multi-threaded** for faster scanning
- Detects open ports
- Clean output with thread-safe printing

---

## 📂 Project Structure

port-scanner/
├── scanner.py # Main script
└── README.md # Project documentation


---

## ✅ Requirements
- Python 3.x
- No external libraries (uses built-in `socket` and `threading`)

---

## ⚡ Usage

### **Run the scanner**
```bash
python3 scanner.py

Example

[*] Enter the targets to scan (split with ,): 192.168.1.10,192.168.1.11
[*] Enter how many ports you want to scan: 100

Output:

[*] Starting Scan for 192.168.1.10
[+] Port Open: 22
[+] Port Open: 80

[*] Starting Scan for 192.168.1.11
[+] Port Open: 22

🛠 How It Works

    Takes input for target IP(s) and port range.

    Creates multiple threads to check each port.

    If a connection is successful → prints [+] Port Open.

    Uses socket.connect_ex() for efficient scanning.