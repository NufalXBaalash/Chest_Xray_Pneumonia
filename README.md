# 🩺 Chest X-ray Pneumonia Detection

This repository contains a Convolutional Neural Network (CNN) model trained to detect pneumonia from chest X-ray images. It includes a trained model and a GUI application for easy predictions.

## 📂 Repository Structure

```
📁 Chest-Xray-Pneumonia-Detection
├── 📜 model.ipynb       # Jupyter Notebook for training the CNN model
├── 📜 Chest_Xray.py      # GUI application using CustomTkinter
├── 📦 Chest_Xray.rar    # Trained model in .h5 format
├── 📜 README.md         # Documentation
```

---

## 📊 Model Training (CNN)

The model is built using TensorFlow/Keras and trained on the **Chest X-ray dataset** from Kaggle: [Chest X-ray Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

- **Architecture**: CNN with convolutional, max-pooling, dropout, and fully connected layers.
- **Input Image Size**: 150x150
- **Activation Function**: ReLU & Sigmoid (for binary classification)
- **Dataset**: Normal vs. Pneumonia X-ray images

📌 *Check `model.ipynb` for the complete training process.*

---

## 🖥️ GUI Application

The `Chest_Xray.py` script provides a **user-friendly GUI** to upload an X-ray image and get predictions.

### 🔧 How to Use:

1. **Install dependencies**:
   ```bash
   pip install customtkinter tensorflow pillow numpy
   ```

2. **Run the application**:
   ```bash
   python Chest_Xray.py
   ```

3. **Upload an X-ray image** using the GUI and get an instant result:
   - ✅ Normal X-ray: "NORMAL Chest X-ray"
   - ❌ Pneumonia Detected: "PNEUMONIA Detected"

### 🎨 GUI Features:
- Built using **CustomTkinter**
- Dark mode theme 🌙
- Simple drag-and-drop file upload

---

## 🚀 Future Improvements
- 📈 Improve model accuracy with more data augmentation
- 🏥 Deploy as a web application for wider accessibility
- 🛠️ Add explainability features (Grad-CAM)

---

## 👨‍💻 Author
**Ahmed Khaled Baalash**

---

⭐ Feel free to fork, star, and contribute!


