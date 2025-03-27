import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator

def load_data(img_size=224, batch_size=32):
    """
    Load and preprocess the image dataset
    """
    # Define data augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    # Define data preprocessing for validation
    val_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )

    # Load training data
    train_generator = train_datagen.flow_from_directory(
        'images',
        target_size=(img_size, img_size),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    # Load validation data
    validation_generator = val_datagen.flow_from_directory(
        'images',
        target_size=(img_size, img_size),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    return train_generator, validation_generator

def get_class_names():
    """
    Get the list of class names from the image directories
    """
    return sorted(os.listdir('images'))

if __name__ == "__main__":
    # Test the data loading
    train_gen, val_gen = load_data()
    print("Number of training samples:", train_gen.samples)
    print("Number of validation samples:", val_gen.samples)
    print("Class names:", get_class_names()) 