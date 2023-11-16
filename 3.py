import io
from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run()
