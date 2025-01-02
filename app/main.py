from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from my_model import load_model, predict
from preprocess import preprocess_image

import numpy as np

# a mettre dans un autre fichier
class prediction (BaseModel): 
    Number: int
    Prediction: dict

app = FastAPI() # port 8000 par defaut
model = load_model('./model/test_model1.h5')

@app.get("/")
def read_root():
    return {"message": "Hello World"}
# routes asynchrone
@app.post("/predict",response_model= prediction)
async def predict_api(file: UploadFile = File(...)):
    try:
        # extraire le fichier
        image = await file.read()

        # traitement de l'image pour le model (resize image ?)
        preprocessed_image = preprocess_image(image)

        # Prédiction à l'aide du modèle
        prediction = predict(model, preprocessed_image)

        rounded_probs = {i: round(prob, 5) for i, prob in enumerate(prediction[0])}

        return {
            # prend le score le plus haut de la liste de proba (health, powdery, rust)
            "Number": np.argmax(prediction[0]),
            "Prediction": rounded_probs
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))