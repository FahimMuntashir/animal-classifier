# 🏆 Custom Image Classification Model for Animal Recognition  
:dog, cow, cat, lamb, and zebra, each with 100 images sourced from the internet or captured using phone. Develop a classification model to classify these classes

**Project Group No.:** 1  
**Group Members:**  
- **Tausib Abrar** (2121446642)  
- **Fahim Muntashir** (2021183642)  
- **Md Abul Bashar Nirob** (2022198042)
- **Muhammad Omar Mahin Jinnat** (2012826642)
---


## 📌 Project Overview  
This project aims to develop a **custom image classification dataset** featuring **five animal classes**:  
🐶 **Dog** | 🐄 **Cow** | 🐱 **Cat** | 🐑 **Lamb** | 🦓 **Zebra**  

We collected **100 images per class** from online sources and personal captures, processed them, and developed a **CNN model** to classify these animals with an accuracy target of **90%+**.

---

## 📂 Dataset Details  
- **Total Images:** **500** (100 per class).  
- **Sources:** Google Images, Unsplash, personal phone captures.  
- **Preprocessing Applied:**  
  - **Resized** → Standardized to **224×224** pixels.  
  - **Normalized** → Scaled pixel values to **[0,1]**.  
  - **Augmented** → Applied **rotation, flipping, cropping** to improve model generalization.  

---

## ⚙️ Model Architecture & Tools  
The model is a **Convolutional Neural Network (CNN)** designed for multi-class classification.  

### **🔧 Libraries Used:**  
- **TensorFlow/Keras** → Model Training  
- **OpenCV** → Image Preprocessing  
- **NumPy & Pandas** → Data Handling  

### **🔍 Model Development Process:**  
1. **Simple CNN Model:** Trained with **500 images** (initial accuracy ~85%).  
2. **Hyperparameter Tuning:** Optimizing **learning rate, batch size, epochs**.  
3. **Transfer Learning (Next Step):** Testing with **pre-trained models** (VGG16, ResNet) for better performance.

---

## 🚀 How to Run the Code  
Follow these steps to run the project:  

### **🔹 Clone the Repository**  
```bash
git clone : (https://github.com/FahimMuntashir/animal-classifier.git)
cd custom-image-classification

🔹 Install Dependencies

pip install -r requirements.txt

🔹 Train the Model

python train.py

🔹 Evaluate the Model

python evaluate.py

📊 Results & Evaluation
	•	Initial CNN Model Accuracy: 85%
	•	Planned Enhancements:
	•	Use Transfer Learning (VGG16, ResNet)
	•	Further tuning of hyperparameters
	•	Increase dataset size for better generalization

🎥 Demo Video

📌 Watch the One-Minute Demo Here 

This demo showcases the model classifying images and its training progress.


📢 Future Work
	•	Experiment with deeper models (EfficientNet, MobileNet).
	•	Optimize preprocessing techniques to improve classification accuracy.
	•	Deploy the model as a web or mobile app for real-time classification.

📖 References
	1.	Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet Classification with Deep Convolutional Neural Networks.
	2.	TensorFlow Documentation: Image Classification Guide

📩 Contact

For any queries, feel free to reach out:
✉️ tausib.abrar@northsouth.edu
