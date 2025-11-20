import os
import hashlib
import json
import qrcode
from datetime import datetime
from fpdf import FPDF

# --- Font paths ---
FONT_PATH_REGULAR = "DejaVuSans.ttf"
FONT_PATH_BOLD = "DejaVuSans-Bold.ttf"

# --- Ensure Certificates folder exists ---
if not os.path.exists("Certificates"):
    os.makedirs("Certificates")


def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def generate_certificate(file_path, file_hash=None):
    """Generate PDF certificate and QR code for a wiped file."""
    if file_hash is None:
        file_hash = calculate_sha256(file_path)

    # --- Prepare certificate data ---
    data = {
        "file_name": os.path.basename(file_path),
        "file_hash": file_hash,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # --- Save JSON ---
    json_path = os.path.join("Certificates", "wipe_certificate.json")
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

    # --- Generate QR code ---
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(data, indent=2))
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_path = os.path.join("Certificates", "wipe_certificate.png")
    qr_img.save(qr_path)

    # --- Generate PDF ---
    pdf = FPDF()
    pdf.add_page()

    # Add Unicode fonts
    pdf.add_font("DejaVu", "", FONT_PATH_REGULAR)
    pdf.add_font("DejaVu", "B", FONT_PATH_BOLD)

    # Title
    pdf.set_font("DejaVu", "B", 16)
    pdf.cell(0, 12, "Secure Wipe Certificate", ln=True, align="C")
    pdf.ln(10)

    # File info
    pdf.set_font("DejaVu", "", 12)
    pdf.multi_cell(0, 8, f"File Name: {data['file_name']}")
    pdf.ln(2)
    pdf.multi_cell(0, 8, f"File Hash:\n{data['file_hash']}")
    pdf.ln(2)
    pdf.multi_cell(0, 8, f"Timestamp (UTC): {data['timestamp']}")
    pdf.ln(5)

    # Insert QR image
    pdf.image(qr_path, x=pdf.get_x() + 60, y=pdf.get_y(), w=50)
    
    # Save PDF
    pdf_path = os.path.join("Certificates", "wipe_certificate.pdf")
    pdf.output(pdf_path)

    print(f"✅ Certificate generated: {pdf_path}")
    return qr_path, pdf_path
