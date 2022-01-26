import numpy as np
import cv2
import matplotlib.pyplot as plt
import base64
from PIL import Image
import io
from src.utils import reshape_image


def handler(model, content):

    cp = CatPrediction(model)
    img = cp.load_img(content)

    output = cp.predict(img)

    return output


class CatPrediction:

    def __init__(self, model):

        self.model = model


    def load_img(self, img_b64):

        img_bytes = base64.b64decode(img_b64.encode('utf-8'))

        img = np.array(Image.open(io.BytesIO(img_bytes))) 

        img = np.expand_dims(reshape_image(img), axis = 0)

        return img

    
    def prepare_output(self, result):

        if result[0][0] > result[0][1]:
            
            output = {
                "result": float(result[0][0]),
                "is_cat": True
            }

        else:
            
            output = {
                "score": float(result[0][1]),
                "is_cat": False
            }

        return output


    def predict(self, img):

        result = self.model.predict(img)

        return self.prepare_output(result)
