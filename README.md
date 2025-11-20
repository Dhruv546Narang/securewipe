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

## 📸 Interface

<div align="center">
  <img src="assets/screenshot.png" alt="GUI Screenshot" width="700" 
       onerror="this.src='https://via.placeholder.com/700x400?text=Upload+screenshot.png+to+assets+folder+to+see+image'" />
</div>

---

## ⚡ Features

| Feature | Description |
| :--- | :--- |
| **🗑️ Secure Wipe** | DoD-standard multi-pass overwriting prevents forensic recovery. |
| **📜 Certificate** | Generates a PDF receipt with SHA-256 hash and timestamp. |
| **📱 QR Verification** | Embeds a QR code in the PDF for instant digital validation. |
| **🖱️ One-Click UI** | Clean, modern Tkinter interface requiring no technical skills. |

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/Dhruv546Narang/securewipe.git](https://github.com/Dhruv546Narang/securewipe.git)
   cd securewipe

2. **Install Dependencies**
```bash
pip install -r requirements.txt

---

## 🚀 Usage

### Method 1: The GUI (Recommended)
Launch the modern one-click interface:
```bash
python src/ui_oneclick_improved.py
