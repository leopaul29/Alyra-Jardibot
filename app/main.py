from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from my_model import load_model, predict
from preprocess import preprocess_image

import numpy as np

# a mettre dans un autre fichier
class prediction (BaseModel): 
    Number: int

app = FastAPI() # port 8000 par defaut
model = load_model('./model/test_model1.h5')

# routes asynchrone
@app.post("/predict",response_model= prediction)
async def predict_api(file: UploadFile = File(...)):
    try:
        # extraire le fichier
        image = await file.read()

        preprocessed_image = preprocess_image(image)
        # traitement de l'image pour le model (resize image ?)

        prediction = predict(model, preprocessed_image)

        return {
            # prend le score le plus de la liste de proba (health, powdery, rust)
            "Number": np.argmax(prediction[0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))