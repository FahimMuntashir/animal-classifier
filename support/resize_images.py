import os
from PIL import Image

# Define the folder containing images
FOLDER_PATH = r"C:\Users\x\Downloads\Projects\animal-classifier\data\Lamb"
SAVE_PATH = os.path.join(FOLDER_PATH, "resized")  # Save resized images in a subfolder

# Create the save directory if it doesn't exist
os.makedirs(SAVE_PATH, exist_ok=True)

# Resize settings
NEW_SIZE = (224, 224)

# Process each image in the folder
for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)
    
    # Ensure it's a file and has an image extension
    if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Convert RGBA/P mode images to RGB
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Resize the image
                img_resized = img.resize(NEW_SIZE, Image.LANCZOS)

                # Save the resized image
                save_file_path = os.path.join(SAVE_PATH, filename)
                img_resized.save(save_file_path)

                print(f"✅ Resized and saved: {save_file_path}")

        except Exception as e:
            print(f"❌ Error resizing {file_path}: {e}")

print(f"🎉 Resizing complete! All images are saved in '{SAVE_PATH}'")
