import os
from PIL import Image, ImageOps


def process_images(input_dir: str, output_dir: str, img_size=(48, 48)):
    """
    Resize, normalize, and correct orientation of images.
    """
    os.makedirs(output_dir, exist_ok=True)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(root, file)

                try:
                    img = Image.open(input_path).convert("L")  # grayscale
                    img = ImageOps.exif_transpose(img)  # fix rotation using EXIF
                    img = img.resize(img_size, Image.LANCZOS)

                    # Normalize pixel values 0–255 → 0–1
                    img = ImageOps.autocontrast(img)

                    # Save processed file
                    rel_dir = os.path.relpath(root, input_dir)
                    out_subdir = os.path.join(output_dir, rel_dir)
                    os.makedirs(out_subdir, exist_ok=True)

                    output_path = os.path.join(out_subdir, file)
                    img.save(output_path)
                except Exception as e:
                    print(f"⚠️ Skipping {file}: {e}")

    print(f"✅ Processed images saved to {output_dir}")
