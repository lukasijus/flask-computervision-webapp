import cv2
import numpy as np
from keras.models import load_model
from keras import backend as K

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './Uploads/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def catOrDog(image):
    '''Determines if the image contains a cat or dog'''
    classifier = load_model('./Models/cats_vs_dogs_V1.h5')
    image = cv2.resize(image, (150, 150), interpolation=cv2.INTER_AREA)
    image = image.reshape(1, 150, 150, 3)
    res = str(classifier.predict_classes(image, 1, verbose=0)[0][0])
    print(res)
    print(type(res))
    if res == "0":
        res = "Cat"
    else:
        res = "Dog"
    K.clear_session()
    return res


def getDominantColor(image):
    '''returns the dominate color among Blue, Green and Reds in the image '''
    B, G, R = cv2.split(image)
    B, G, R = np.sum(B), np.sum(G), np.sum(R)
    color_sums = [B, G, R]
    color_values = {"0": "Blue", "1": "Green", "2": "Red"}
    return color_values[str(np.argmax(color_sums))]