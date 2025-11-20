import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from secure_wipe import secure_wipe
import cert_utils

# --- Colors & Fonts ---
BG_COLOR = "#1e1e2f"
BTN_COLOR = "#4a90e2"
BTN_HOVER = "#357ABD"
BTN_TEXT = "#ffffff"
WIPE_BTN_COLOR = "#e94f4f"
WIPE_BTN_HOVER = "#c43c3c"
FONT_TITLE = ("Arial", 20, "bold")
FONT_LABEL = ("Arial", 12)
FONT_BTN = ("Arial", 12, "bold")

# --- Tkinter Setup ---
root = tk.Tk()
root.title("SecureWipe - One Click")
root.geometry("750x400")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# --- Left Frame: Logo + Buttons ---
left_frame = tk.Frame(root, bg=BG_COLOR)
left_frame.pack(side="left", fill="y", padx=20, pady=20)

# Logo
logo_path = "logo.png"
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((120, 120), Image.Resampling.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(left_frame, image=logo_tk, bg=BG_COLOR)
    logo_label.pack(pady=(10, 30))
else:
    logo_label = tk.Label(left_frame, text="SecureWipe", font=FONT_TITLE, fg="#ffffff", bg=BG_COLOR)
    logo_label.pack(pady=(20, 30))

# Buttons
selected_file = None
def on_enter(e, btn, hover_color):
    btn['bg'] = hover_color

def on_leave(e, btn, normal_color):
    btn['bg'] = normal_color

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_status_label.config(text=f"Selected:\n{os.path.basename(selected_file)}")

def wipe_file():
    global selected_file
    if not selected_file:
        messagebox.showwarning("Warning", "Please select a file first!")
        return
    try:
        file_hash = secure_wipe(selected_file)
        if not file_hash:
            messagebox.showerror("Error", "Failed to wipe the file.")
            return
        qr_path, pdf_path = cert_utils.generate_certificate(selected_file, file_hash)
        file_status_label.config(text=f"Wiped:\n{os.path.basename(selected_file)}")
        messagebox.showinfo("Success", f"File securely wiped!\nCertificate generated:\n{pdf_path}")
        show_qr_preview(qr_path)
        selected_file = None
    except Exception as e:
        messagebox.showerror("Error", str(e))

select_btn = tk.Button(left_frame, text="Select File", command=select_file, width=20, bg=BTN_COLOR, fg=BTN_TEXT, font=FONT_BTN, relief="raised", bd=3)
select_btn.pack(pady=10)
select_btn.bind("<Enter>", lambda e: on_enter(e, select_btn, BTN_HOVER))
select_btn.bind("<Leave>", lambda e: on_leave(e, select_btn, BTN_COLOR))

wipe_btn = tk.Button(left_frame, text="Wipe File", command=wipe_file, width=20, bg=WIPE_BTN_COLOR, fg=BTN_TEXT, font=FONT_BTN, relief="raised", bd=3)
wipe_btn.pack(pady=10)
wipe_btn.bind("<Enter>", lambda e: on_enter(e, wipe_btn, WIPE_BTN_HOVER))
wipe_btn.bind("<Leave>", lambda e: on_leave(e, wipe_btn, WIPE_BTN_COLOR))

# --- Right Frame: File Status + QR ---
right_frame = tk.Frame(root, bg=BG_COLOR)
right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

file_status_label = tk.Label(right_frame, text="No file selected", font=FONT_LABEL, fg="#ffffff", bg=BG_COLOR, justify="center")
file_status_label.pack(pady=(20, 10))

qr_label = tk.Label(right_frame, bg=BG_COLOR)
qr_label.pack(pady=10)

def show_qr_preview(qr_path):
    if os.path.exists(qr_path):
        img = Image.open(qr_path)
        img = img.resize((180, 180), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

root.mainloop()
