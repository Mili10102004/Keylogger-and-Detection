
A *keylogger* records keystrokes on a keyboard. This tool demonstrates:
- How to monitor user input with pynput
- Sending data securely via SMTP and Python's email libraries
- Building standalone executables using PyInstaller
- Understanding security risks and responsible disclosure

> ⚠ *Disclaimer: This project is strictly for educational, research, or ethical monitoring (e.g., personal device logging with consent). Unauthorized use is **illegal and unethical*.

---

## 📁 Folder Structure
test2/
├── build/ # Intermediate files from PyInstaller
│ └── keylogger_email/
├── dist/ # Final packaged executable
│ ├── keylogger_email.exe # The keylogger executable
│ ├── start.bat # Launcher batch file
│ └── test.jpg # Decoy image
├── venv/ # Python virtual environment
└── keylogger_email.py # 🔑 Main Python script

---

## 🛠 Setup Instructions (For Development)

### 1. Clone or Extract Project

```bash
unzip test2.zip
cd test2

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install pynput
