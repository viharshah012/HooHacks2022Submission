from flask import Flask, request
import io
import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

app = Flask(__name__)


# Members API route
@app.route("/members", methods = ['POST'])
def members():
    credential_path = r"apikey.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    client = vision_v1.ImageAnnotatorClient()

    file = request.form['picture']
    with io.open(file, "rb") as img_file:
        content = img_file.read()
    
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    descr = list()
    for i in labels:
        descr.append(i.description)

    materials = ["Cardboard", "Tin", "Aluminium", "Glass bottle", "Beer bottle",
                "Plastic bottle", "Box", "Paper product", "Paper"]
    recycle = [value for value in descr if value in materials]
    links = {}

    with open("link.txt") as file:
        for i in file.readlines():
            item = i.split(",")[0]
            if (item in recycle):
                links[item] = i.strip("\n").split(",")[1:]
    return links


if __name__ == "__main__":
    app.run(debug=True)