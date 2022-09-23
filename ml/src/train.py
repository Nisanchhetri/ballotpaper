import numpy as np

from model.prepare_model import loading_model
from src.predict import predict_labels

def pretrained_model():
    print("Please select the model for classification:\n")
    selected_model = input("1.MobileNet\n2.LeNet (CNN model)\n")
    model = loading_model(model_para=selected_model)
    image_array = input("Please enter the image array:\n")
    predicted_labels = predict_labels(model=model, input_image=image_array)
    print("The labels of your input image is: ", predicted_labels)