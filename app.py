from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("diabetes_model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        glucose = float(request.form['glucose'])
        hba1c = float(request.form['hba1c'])
        hypertension = float(request.form['hypertension'])
        heart_disease = float(request.form['heart_disease'])
        gender = float(request.form['gender'])
        smoking = float(request.form['smoking'])

        # Array for model input (must match training order)
        features = np.array([[gender, age, hypertension, heart_disease, smoking, bmi, hba1c, glucose]])

        prediction = model.predict(features)
        result = "High Diabetes Risk" if prediction[0] == 1 else "Low / No Diabetes Risk"

        return render_template("index.html", prediction_text=result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


