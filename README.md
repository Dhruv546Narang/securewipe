<div align="center">

  <img src="assets/logo.png" alt="SecureWipe Logo" width="200" />
  
  # SecureWipe
  
  **The One-Click Secure File Erasure Tool**
  
  <p>
    A professional Python utility that performs <b>multi-pass secure overwriting</b><br />
    and generates verifiable <b>PDF Certificates</b> as proof of destruction.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/GUI-Tkinter-2C2D72?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Security-Cryptography-red?style=for-the-badge&logo=security&logoColor=white" />
  </p>

  <p>
    <a href="#-installation">Installation</a> •
    <a href="#-usage">Usage</a> •
    <a href="#%EF%B8%8F-security-disclaimer">Disclaimer</a>
  </p>

</div>

---

## ⚡ Features

| Feature | Description |
| :--- | :--- |
| **🗑️ Secure Wipe** | Multi-pass overwriting prevents forensic recovery. |
| **📜 Certificate** | Generates a PDF receipt with SHA-256 hash and timestamp. |
| **📱 QR Verification** | QR code included in PDF for instant authenticity check. |
| **🖱️ One-Click UI** | Clean Tkinter interface for non-technical users. |

---

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Dhruv546Narang/securewipe.git
cd securewipe
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Method 1 — GUI (Recommended)
```bash
python src/ui_oneclick_improved.py
```

### Method 2 — Script Integration
```python
from src.secure_wipe import secure_wipe
secure_wipe("sensitive_data.txt", passes=3)
```

## 📂 Project Structure
```bash
securewipe/
├── assets/               # Logo and images
├── Certificates/         # Auto-generated certificates
├── src/
│   ├── secure_wipe.py    # Secure wipe engine
│   ├── cert_utils.py     # QR + PDF generator
│   ├── generate_key.py   # RSA key tool
│   └── ui_oneclick_improved.py  # GUI
├── requirements.txt
└── README.md
```

## ⚠️ Security Disclaimer

While SecureWipe implements standard overwriting methods, **perfect data destruction is not always guaranteed** on:

- SSDs / NVMe
- Journaling filesystems (NTFS, APFS, ext4, etc.)
- Cloud-synced folders
- Drives with snapshots / backups

For critical erasure: **physical destruction is the only 100% secure method.**
