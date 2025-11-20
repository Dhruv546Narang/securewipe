📄 SecureWipe – File Erasure & Certificate Generator

SecureWipe is a Python-based utility designed to securely erase files through multi-pass overwriting and generate digital proof-of-wipe certificates.
It includes a simple one-click GUI, SHA-256 hashing, QR-code embedding, and PDF generation — all neatly bundled in an accessible interface.

🚀 Features

🔐 Secure Multi-Pass File Wipe

🧾 PDF Certificate Generation

📡 QR Code Embedded Metadata

🖥️ One-Click Tkinter GUI

🔑 RSA Key Generator (optional)

📂 Clean Project Structure

🧰 Tech Stack

Python 3

Tkinter (GUI)

Pillow (Image handling)

Cryptography (Key generation)

FPDF (Certificate PDF)

qrcode (QR code generator)

📁 Project Structure
SecureWipe/
│
├── src/
│   ├── secure_wipe.py
│   ├── cert_utils.py
│   ├── generate_key.py
│   └── ui_oneclick_improved.py
│
├── assets/
│   └── logo.png
│
├── Certificates/      # auto-generated after wiping
│   └── ...
│
├── requirements.txt
└── README.md

🖼️ Screenshots

(Add your GUI screenshots here)
Example:


⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/SecureWipe.git
cd SecureWipe

2️⃣ Install Requirements
pip install -r requirements.txt

🧪 Usage Guide
▶ Run the GUI
python src/ui_oneclick_improved.py

▶ Programmatic Wipe
from secure_wipe import secure_wipe
secure_wipe("file.txt", passes=3)

▶ Generate RSA Keys
python src/generate_key.py

⚠️ Security Disclaimer

SecureWipe attempts multi-pass overwriting but cannot guarantee absolute deletion on:

SSDs

Journaling or copy-on-write filesystems

Cloud-synced locations

Devices with snapshots/backups

Use responsibly.

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.
You can change it if needed.

📬 Contact

If you have questions or need help integrating SecureWipe:
Dhruv Narang
Email: dhruv546narang.com
