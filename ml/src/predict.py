import numpy as np

def predict_labels(model=None, input_image=None):
    raw_labels = model.predict(input_image)
    predicted_labels = np.argmax(raw_labels, axis=1)
    return predicted_labels