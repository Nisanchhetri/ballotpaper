from tensorflow.keras.preprocessing.image import image
def process_image(input_image=None):
    img = image.img_to_array(img)
    img = (img/127.5) - 1
    return img