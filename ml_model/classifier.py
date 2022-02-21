import cv2
import numpy as np
import json
from keras.models import load_model

class ImageClassifier():
    def __init__(self, img_link):
        self.img = cv2.imread(img_link)
        self.img_shape = (400, 400)
        self.confidence = None

    def preprocess_img(self):
        self.img = np.float32(self.img)
        self.crop_image()
        self.img = np.expand_dims(self.img, axis=0)
        self.img = (self.img - self.img.min()) / (self.img.max() - self.img.min())
        return self.img

    def crop_image(self, min_size=200):
        img = self.img
        x, y = img.shape[0], img.shape[1]
        size = max(min_size, x, y)
        new_img = np.zeros((size, size, 3), np.uint8)
        new_img[((size - x) // 2):(size + x) // 2, (size - y) // 2:(size + y) // 2] = img
        new_img = cv2.resize(new_img,self.img_shape,cv2.INTER_AREA)
        self.img =  new_img

    def load_model(self):
        self.model = load_model('./ml_model/final_model_high_res.h5')
        with open('./ml_model/class_dictionary.json','r') as f:
            self.img_classes = json.load(f)
            self.img_classes = {v:k for k,v in self.img_classes.items()}

    def predict(self):
        probabilities = np.round(self.model.predict(self.preprocess_img()), 3)[0]
        self.probabilities = [str(round(x*100))+'%' for x in probabilities]
        self.prediction = self.img_classes[np.argmax(np.append(probabilities, 0.6))]
        self.confidence = str(round(probabilities.max()*100))+'%'

    def get_predictions(self):
        results = {
            'Class': self.prediction,
            'Confidence': self.confidence,
            'Probabilities': dict(zip(self.img_classes.values(),self.probabilities))
        }
        return results

