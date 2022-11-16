from numpy import argmax
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model

def load_image(filename):
    test_img = load_img(filename, grayscale=True, target_size=(28, 28))
    img = img_to_array(test_img)
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32')
    img = img / 255.0
    return img,test_img

def predict():
    img,test_img = load_image('sample_image-768x763.png')
    model = load_model('model/model.h5')

    predict_value = model.predict(img)
    digit = argmax(predict_value)
    print(digit)
    return test_img