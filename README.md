<div align="center">

  <br />
  <img src="assets/logo.png" alt="SecureWipe Logo" width="150" height="auto" />
  
  <h1>SecureWipe</h1>
  
  <p>
    <b>Professional Grade File Erasure & Certification Tool</b>
  </p>
  
  <p>
    A Python utility that performs <b>multi-pass secure overwriting</b> of files and generates <br />
    cryptographically verifiable <b>PDF Certificates</b> as proof of destruction.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/GUI-Tkinter-2C2D72?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter" />
    <img src="https://img.shields.io/badge/Security-Cryptography-red?style=for-the-badge&logo=security&logoColor=white" alt="Security" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  </p>

  <p>
    <a href="#-features">Features</a> •
    <a href="#-installation">Installation</a> •
    <a href="#-usage">Usage</a> •
    <a href="#%EF%B8%8F-security-disclaimer">Disclaimer</a>
  </p>

</div>

---

## ⚡ Features

* **🗑️ DoD-Style Wiping:** Performs multi-pass overwriting to ensure data is unrecoverable by forensics tools.
* **📜 Proof of Deletion:** Automatically generates a **PDF Certificate** containing the file's SHA-256 hash and timestamp.
* **📱 QR Code Verification:** Embeds a QR code in the certificate for instant digital verification.
* **🖱️ One-Click Interface:** Simple, clean GUI built with Tkinter — no command line knowledge required.
* **🔐 RSA Signed:** Includes utilities to generate RSA keys for digitally signing the deletion logs.

---

## 📸 Screenshots

<div align="center">
  <img src="https://via.placeholder.com/800x450?text=Add+Application+Screenshot+Here" alt="SecureWipe Interface" />
</div>

---

## 🛠️ Installation

### Prerequisites
Ensure you have **Python 3.8** or higher installed on your system.

### 1. Clone the Repository
```bash
git clone [https://github.com/Dhruv546Narang/securewipe.git](https://github.com/Dhruv546Narang/securewipe.git)
cd securewipe
2. Install Dependencies
Bash

pip install -r requirements.txt
🚀 Usage
Method 1: The GUI (Recommended)
Launch the modern one-click interface:

Bash

python src/ui_oneclick_improved.py
Method 2: Script Integration
You can import the wiper module into your own Python automation scripts:

Python

from src.secure_wipe import secure_wipe

# Wipe a specific file with 3 passes (DoD standard)
secure_wipe("sensitive_data.txt", passes=3)
📂 Project Structure
Plaintext

securewipe/
├── assets/                  # Logos and UI resources
├── Certificates/            # Generated proof-of-wipe PDFs go here
├── src/                     # Source Code
│   ├── secure_wipe.py       # Core wiping logic (Multi-pass overwrite)
│   ├── cert_utils.py        # PDF & QR Code generation engine
│   ├── generate_key.py      # RSA Key generation utility
│   └── ui_oneclick_improved.py  # Main GUI entry point
├── requirements.txt         # Python dependencies
└── README.md                # Documentation
⚠️ Security Disclaimer
Note: While SecureWipe implements standard overwriting techniques, absolute data destruction on Modern SSDs and Journaling File Systems (like NTFS, APFS, or ext4) cannot be guaranteed by software alone due to hardware-level wear-leveling and block reallocation.

For critical hardware decommissioning, physical destruction of the drive is the only 100% guaranteed method.
