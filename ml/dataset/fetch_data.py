import pandas as pd
import numpy as np

from tensorflow.keras.preprocessing.image import ImageDataGenerator

from configs.configs import *

def load_data():
    print("Loading dataset........\n")
    df_train = pd.read_csv(train_csv_path, dtype=str)
    df_test = pd.read_csv(test_csv_path, dtype=str)

    train_dataGen = ImageDataGenerator(
                    rescale = 1./255,
                    rotation_range=40,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range = 0.2,
                    zoom_range = 0.2
                  )

    test_dataGen = ImageDataGenerator(rescale = 1./255)

    train_generator = train_dataGen.flow_from_dataframe(
                      dataframe = df_train,
                      directory=train_images_path,
                      x_col="Data",
                      y_col="Label",
                      class_mode="categorical",
                      target_size=(150,150),
                      batch_size=32
                    )

    test_generator = test_dataGen.flow_from_dataframe(
                      dataframe=df_test,
                      directory=test_images_path,
                      x_col="Data", y_col="Label",
                      class_mode="categorical",
                      target_size=(150,150),
                      batch_size=32
                    )
    print("Dataset sucessfully loaded!!\n")
    return train_generator, test_generator