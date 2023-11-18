import pickle
from flask import Flask, request
from PIL import Image
from tensorflow import convert_to_tensor, expand_dims
from tensorflow import keras
import numpy as np

app = Flask(__name__)

with open("models/model.pkl", "rb") as f:
    lr = pickle.load(f)


IMAGE_SIZE = (180, 180)
model = keras.models.load_model("models/cats_dogs.h5")


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/echo", methods=["POST"])
def echo():
    param = request.get_json()
    return param


@app.route("/upload_image", methods=["POST"])
def upload_image():
    img_bin = request.files["image"]
    img = Image.open(img_bin)
    return {"width": img.width, "height": img.height}


@app.route("/predict_score")
def predict_score():
    hours = request.args.get("hours")
    if not hours.isdigit():
        return {"error_message": "숫자를 입력하세요."}

    score = lr.predict([[int(hours)]])
    return {"score": score[0]}


@app.route("/predict_cats_dogs", methods=["POST"])
def predict_cats_dogs():
    img_bin = request.files["image"]
    img = Image.open(img_bin)
    img.resize(IMAGE_SIZE)
    img_array = convert_to_tensor(img)
    img_array = expand_dims(img_array, 0)

    pred = model.predict(img_array)
    score = float(pred[0])
    return {
        "result": f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog."
    }


if __name__ == "__main__":
    app.run()
