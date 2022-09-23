from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

from .store_model import pretrained_models
from configs.configs import *

def generate_cnn_model():
    '''LetNet architecture'''
    model = Sequential()
    model.add(Conv2D(
        filters=32, kernel_size=(3, 3),
        activation="relu", input_shape=(150,150,3))
    )
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(48, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                )

    return model

def loading_model(model_para='1'):
    try:
        model_name = pretrained_models.get(model_para)
        model_abs_path = os.path.join(MODEL_PATH, model_name + ".h5")
        print("You have selected ", model_name)
        print("\nLoading the model...............")
        loaded_model = load_model(model_abs_path)
        print("\nModel loading completed!!\n")
        return loaded_model
    except:
        print("Please select the valid model!!")