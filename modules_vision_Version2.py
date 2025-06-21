from PIL import Image

def image_to_text(image: Image.Image) -> str:
    # Demo: bisa diintegrasikan dengan BLIP, Tesseract, Google Vision, dsb
    # Untuk sekarang, return dummy caption
    return "Gambar berhasil diunggah (fitur deskripsi otomatis bisa ditambah)"