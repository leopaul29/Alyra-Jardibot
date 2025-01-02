import numpy as np
from PIL import Image
import io

def preprocess_image(image):
    img = Image.open(io.BytesIO(image))
    # img_array = np.array(img)
    img_resized = img.resize((224,224))
    # img_gray = img_resized.convert('L') # convert en gris
    img_rgb = img_resized.convert('RGB') # convert en palette de couleur
    # img_array = np.array(img_gray)
    img_array = np.array(img_rgb) / 255.0

    # img_final = img_array.reshape(1,784).astype("float32")
    # img_final = img_array.astype("float32")

    # Ajouter une dimension pour le batch size
    img_final = np.expand_dims(img_array, axis=0)  # Shape: (1, 224, 224, 3)

    return img_final