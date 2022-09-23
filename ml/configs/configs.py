import os

ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))

dataset_path = os.path.join(ROOT_DIR, 'ml/data/external/')
train_csv_path = os.path.join(dataset_path, 'Train/testset.csv')
test_csv_path = os.path.join(dataset_path, 'Test/testset.csv')
train_images_path = os.path.join(dataset_path, 'Train/testset/')
test_images_path = os.path.join(dataset_path, 'Test/testset/')

inception_model_path = os.path.join(ROOT_DIR, 'ml/saved_model/inception_model.h5')
cnn_model_path = os.path.join(ROOT_DIR, 'ml/saved_model/cnn_model.h5')
dense_model_path = os.path.join(ROOT_DIR, 'ml/saved_model/dense_model.h5')
mobile_model_path = os.path.join(ROOT_DIR, 'ml/saved_model/mobile_model.h5')

MODEL_PATH = os.path.join(ROOT_DIR, 'ml/saved_model/')