import numpy as np
from PIL import Image
import io

def preprocess_image(image):
    img = Image.open(io.BytesIO(image))
    # img_resized = img.resize((28,28))
    # img_gray = img_resized.convert('L') # convert en gris
    # img_array = np.array(img_gray)
    img_array = np.array(img)
    # img_final = img_array.reshape(1,784).astype("float32")
    img_final = img_array.astype("float32")

    return img_final