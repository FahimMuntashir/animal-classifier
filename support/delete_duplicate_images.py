import os
import hashlib
from collections import defaultdict

# Define folder path
FOLDER_PATH = r"C:\Users\x\Downloads\Projects\animal-classifier\data\Cow"

# Dictionary to store image hashes
hashes = defaultdict(list)

def get_image_hash(file_path):
    """Computes SHA-256 hash of an image file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Scan images in the folder
for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)

    if os.path.isfile(file_path):  # Ensure it's a file
        img_hash = get_image_hash(file_path)
        hashes[img_hash].append(file_path)  # Store all images with the same hash

# Delete duplicates and keep only one image per group
duplicates_deleted = 0

for group in hashes.values():
    if len(group) > 1:
        # Keep the first image, delete the rest
        for img_path in group[1:]:
            try:
                os.remove(img_path)
                duplicates_deleted += 1
                print(f"❌ Deleted duplicate: {img_path}")
            except Exception as e:
                print(f"Error deleting {img_path}: {e}")

print(f"🎉 Total {duplicates_deleted} duplicate images deleted!")
