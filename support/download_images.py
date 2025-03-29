import os
import requests
from duckduckgo_search import DDGS

# Define save path
SAVE_PATH = r"C:\Users\x\Downloads\Projects\animal-classifier\data\Cow"
os.makedirs(SAVE_PATH, exist_ok=True)

# Download images with retry logic
def download_images(query, total_images, save_path):
    downloaded = 0
    batch_size = 50  # Fetch images in batches
    attempt = 1

    with DDGS() as ddgs:
        while downloaded < total_images:
            print(f"Attempt {attempt}: Fetching more images...")

            # Fetch new images (adjust batch size to prevent duplicates)
            results = list(ddgs.images(query, max_results=batch_size))

            for img in results:
                if downloaded >= total_images:
                    break

                img_url = img["image"]
                try:
                    img_data = requests.get(img_url, timeout=5)
                    img_data.raise_for_status()

                    file_path = os.path.join(save_path, f"cow_{downloaded + 1}.jpg")

                    with open(file_path, "wb") as f:
                        f.write(img_data.content)

                    downloaded += 1
                    print(f"✅ Downloaded: {file_path}")

                except Exception as e:
                    print(f"❌ Failed to download {img_url}: {e}")

            attempt += 1

    print(f"🎉 Download complete! Total images downloaded: {downloaded}")

# Download 100 cow images
download_images("cow", 100, SAVE_PATH)
