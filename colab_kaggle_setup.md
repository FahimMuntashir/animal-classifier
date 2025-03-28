# Running Animal Classifier on Google Colab and Kaggle

This guide will help you run the Animal Classifier project on Google Colab and Kaggle platforms.

## 🚀 Google Colab Setup

1. **Create a new Colab notebook**

   - Go to [Google Colab](https://colab.research.google.com/)
   - Create a new notebook

2. **Mount Google Drive**

```python
from google.colab import drive
drive.mount('/content/drive')
```

3. **Clone the repository**

```python
!git clone https://github.com/FahimMuntashir/animal-classifier.git
%cd animal-classifier
```

4. **Install dependencies**

```python
!pip install -r requirements.txt
```

5. **Run the web application using ngrok**

```python
# Install ngrok
!pip install pyngrok

# Start the Flask app with ngrok
from pyngrok import ngrok
from app import app
import threading

# Start ngrok
public_url = ngrok.connect(5000).public_url
print(f' * Public URL: {public_url}')

# Run Flask app in a separate thread
threading.Thread(target=app.run, kwargs={'use_reloader': False}).start()
```

## 🎯 Kaggle Setup

1. **Create a new Kaggle notebook**

   - Go to [Kaggle](https://www.kaggle.com/)
   - Create a new notebook

2. **Clone the repository**

```python
!git clone https://github.com/FahimMuntashir/animal-classifier.git
%cd animal-classifier
```

3. **Install dependencies**

```python
!pip install -r requirements.txt
```

4. **Run the web application using ngrok**

```python
# Install ngrok
!pip install pyngrok

# Start the Flask app with ngrok
from pyngrok import ngrok
from app import app
import threading

# Start ngrok
public_url = ngrok.connect(5000).public_url
print(f' * Public URL: {public_url}')

# Run Flask app in a separate thread
threading.Thread(target=app.run, kwargs={'use_reloader': False}).start()
```

## 📝 Important Notes

### For Both Platforms:

1. **Data Storage**

   - Upload your dataset to Google Drive (for Colab) or Kaggle Datasets
   - Update the data paths in the code accordingly

2. **Model Storage**

   - Save trained models to Google Drive or Kaggle Datasets
   - Update model paths in the code

3. **Session Duration**

   - Colab sessions expire after 12 hours
   - Kaggle sessions have time limits
   - Save your work frequently

4. **GPU Usage**
   - Both platforms provide free GPU access
   - Enable GPU in runtime settings
   - Check GPU availability:

```python
import tensorflow as tf
print("GPU Available:", tf.config.list_physical_devices('GPU'))
```

### Platform-Specific Tips:

#### Google Colab

- Use `!pip install` for package installation
- Use `%cd` for directory changes
- Use `!git clone` for repository cloning
- Save notebooks to Google Drive

#### Kaggle

- Use Kaggle Datasets for data storage
- Enable internet access in notebook settings
- Use Kaggle's GPU quota efficiently

## 🔧 Troubleshooting

1. **Connection Issues**

   - Check internet connection
   - Verify ngrok tunnel status
   - Restart runtime if needed

2. **Memory Issues**
   - Clear memory:

```python
import gc
gc.collect()
```

- Use smaller batch sizes
- Monitor GPU memory usage

3. **Package Installation Issues**
   - Try installing packages one by one
   - Use specific package versions
   - Check compatibility with platform

## 📊 Performance Optimization

1. **GPU Utilization**

```python
# Enable mixed precision training
tf.keras.mixed_precision.set_global_policy('mixed_float16')
```

2. **Memory Management**

```python
# Limit GPU memory growth
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
```

## 🔗 Useful Links

- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [Kaggle Documentation](https://www.kaggle.com/docs)
- [Project GitHub Repository](https://github.com/FahimMuntashir/animal-classifier)
