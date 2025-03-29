import os

# Define folder path containing the images
FOLDER_PATH = r"C:\Users\x\Downloads\Projects\animal-classifier\data\Cow"

# Get all files in the folder
files = os.listdir(FOLDER_PATH)

# Filter out only image files (you can extend this if needed)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
images = [file for file in files if any(file.lower().endswith(ext) for ext in image_extensions)]

# Rename images sequentially
for i, image in enumerate(images, 1):
    old_path = os.path.join(FOLDER_PATH, image)
    new_name = f"cow_{i}{os.path.splitext(image)[1]}"  # Add the original extension
    new_path = os.path.join(FOLDER_PATH, new_name)

    # Rename the image
    os.rename(old_path, new_path)
    print(f"Renamed: {old_path} to {new_path}")

print(f"🎉 Renaming complete! Total {len(images)} images renamed.")
