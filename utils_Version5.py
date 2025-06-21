# Modul utilitas: integrasi AI & vision
import requests

# Fungsi untuk tanya AI (gunakan API open source atau trial gratis)
def ask_ai(prompt, history=None):
    # Contoh: gunakan OpenAI API gratis (isi dengan key Anda) atau model lokal
    # Untuk demo, hanya membalas echo
    return f"Jawaban AI untuk: {prompt[:100]} ... (demo, integrasi model asli di sini)"

# Fungsi buat mengubah gambar jadi teks (OCR atau image captioning)
def image_to_text(image):
    # Untuk demo, pakai placeholder
    return "Deskripsi otomatis gambar (fitur bisa pakai Tesseract, BLIP, dll)"