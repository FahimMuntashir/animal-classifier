import os
import random
from PIL import Image, ImageEnhance

# Define the folder containing images
FOLDER_PATH = r"C:\Users\x\Downloads\Projects\animal-classifier\data\Lamb"
SAVE_PATH = os.path.join(FOLDER_PATH, "augmented")  # Save augmented images in a subfolder

# Create the save directory if it doesn't exist
os.makedirs(SAVE_PATH, exist_ok=True)

# Define transformations
def mirror(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def rotate_left(img):
    return img.rotate(90, expand=True)

def rotate_right(img):
    return img.rotate(-90, expand=True)

def rotate_upside_down(img):
    return img.rotate(180)

def brighten(img, factor=1.5):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def darken(img, factor=0.5):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

# List of available transformations
TRANSFORMATIONS = [mirror, rotate_left, brighten, rotate_right, darken, rotate_upside_down]

# Process each image in the folder
for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)

    # Ensure it's a file and has an image extension
    if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Convert RGBA/P mode images to RGB to avoid saving issues
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Randomly select 3 unique transformations
                selected_transforms = random.sample(TRANSFORMATIONS, 3)

                # Get image base name without extension
                base_name, ext = os.path.splitext(filename)

                # Apply and save transformations
                for i, transform in enumerate(selected_transforms, 1):
                    augmented_img = transform(img)  # Apply transformation
                    save_file_path = os.path.join(SAVE_PATH, f"{base_name}_{i}{ext}")
                    augmented_img.save(save_file_path)  # Save image
                    print(f"✅ Created: {save_file_path}")

        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

print(f"🎉 Augmentation complete! All images are saved in '{SAVE_PATH}'")
