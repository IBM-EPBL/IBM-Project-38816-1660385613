from flask import Flask, render_template, request

import make_prediction

app = Flask(__name__)



@app.route('/',methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imageFile = request.files['imagefile']
    imgPath = "./images/"+imageFile.filename
    imageFile.save(imgPath)
    # arr = np.array([[data1, data2, data3, data4]])
    pred = make_prediction.predict()
    return render_template('index.html', prediction= pred)


if __name__ == "__main__":
    app.run(debug=True)















