import tensorflow as tf
import numpy as np
from PIL import Image
from preprocess import get_class_names

def preprocess_image(image_path, img_size=224):
    """
    Preprocess a single image for prediction
    """
    # Load and resize image
    img = Image.open(image_path)
    img = img.resize((img_size, img_size))
    
    # Convert to array and preprocess
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict_image(model_path, image_path):
    """
    Make prediction on a single image
    """
    # Load the model
    model = tf.keras.models.load_model(model_path)
    
    # Get class names
    class_names = get_class_names()
    
    # Preprocess image
    img_array = preprocess_image(image_path)
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    
    return predicted_class, confidence

def main():
    # Example usage
    model_path = 'best_model.h5'
    image_path = input("Enter the path to the image you want to classify: ")
    
    try:
        predicted_class, confidence = predict_image(model_path, image_path)
        print(f"\nPredicted class: {predicted_class}")
        print(f"Confidence: {confidence:.2%}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 