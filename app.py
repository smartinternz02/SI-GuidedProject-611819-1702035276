import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__, template_folder='templates')
model = pickle.load(open("./Randf.pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template('home.html')

@flask_app.route('/predict.html')
def prediction():
    return render_template('predict.html')

@flask_app.route('/about.html')
def about():
    return render_template('about.html')

@flask_app.route('/submit.html')
def submit():
    return render_template('submit.html')


@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if(prediction == 0):
        ans = "Might not be successful"
    else:
        ans = "Might be successful"
    return render_template("submit.html", prediction_text = "The company: {}".format(ans))

if __name__ == "__main__":
    flask_app.run(debug=True)