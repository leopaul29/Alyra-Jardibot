import tensorflow as tf

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def predict(model, image):
    prediction = model.predict(image)

    # donne une liste de prediction ordonné par score
    return prediction.tolist()
