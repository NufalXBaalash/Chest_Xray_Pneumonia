import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model("Chest_Xray.h5")

# Function to process and predict the image
def predict_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    if not file_path:
        return  # If no file is selected, return

    # Load and preprocess the image
    img = image.load_img(file_path, target_size=(150, 150))  # Adjust size if needed
    img_array = image.img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions for model input

    # Get prediction
    prediction = model.predict(img_array)[0][0]
    
    # Display image
    img_display = Image.open(file_path)
    img_display = img_display.resize((300, 300))  # Resize for display
    img_display = ImageTk.PhotoImage(img_display)
    image_label.configure(image=img_display)
    image_label.image = img_display  # Keep reference

    # Display result
    if prediction > 0.5:
        result_label.configure(text="PNEUMONIA Detected ❌", text_color="red")
    else:
        result_label.configure(text="NORMAL Chest X-ray ✅", text_color="green")

# Create the GUI window
ctk.set_appearance_mode("dark")  # Options: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Color themes: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Chest X-ray Predictor")
root.geometry("450x600")

# Heading
title_label = ctk.CTkLabel(root, text="Chest X-ray Predictor", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Image display
image_label = ctk.CTkLabel(root, text="No Image Selected", width=300, height=300, fg_color="gray", corner_radius=10)
image_label.pack(pady=10)

# Upload button
upload_btn = ctk.CTkButton(root, text="Upload X-ray", command=predict_image, font=("Arial", 14))
upload_btn.pack(pady=20)

# Prediction result
result_label = ctk.CTkLabel(root, text="Prediction: ", font=("Arial", 16))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
