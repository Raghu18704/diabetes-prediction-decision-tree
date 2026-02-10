from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__)


model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    
    gender = 1 if request.form["gender"] == "Male" else 0

    smoking_map = {
        "never": 0,
        "former": 1,
        "current": 2
    }
    smoking = smoking_map[request.form["smoking_history"]]

    data = [
        gender,
        int(request.form["age"]),
        int(request.form["hypertension"]),
        int(request.form["heart_disease"]),
        smoking,
        float(request.form["bmi"]),
        float(request.form["HbA1c_level"]),
        int(request.form["blood_glucose_level"])
    ]

    prediction = model.predict([data])[0]

    result = "Diabetes Detected" if prediction == 1 else "No Diabetes"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)
