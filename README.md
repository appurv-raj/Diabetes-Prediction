🩺 Diabetes Prediction Web App:
A machine learning web application to predict diabetes risk based on medical and lifestyle inputs.
Built using Python, Flask, and Machine Learning (Logistic Regression).

✅ Features:
ML Model trained (Accuracy: 96%)

Real-time prediction from user inputs

Clean Flask frontend

Model saved using Pickle (model.pkl)

Project Structure:
├── app.py <br>
├── model.pkl <br>
├── static/ <br>
│   └── style.css <br>
└── templates/ <br>
    └── index.html

Setup & Run:
Install requirements
pip install -r requirements.txt

Run server:
python app.py

Open in browser:
http://127.0.0.1:5000/

📊 Model Info:
Algorithm: Logistic Regression

Dataset: Diabetes Prediction Dataset (Cleaned)

80/20 Train-Test Split

Saved as model.pkl

🔮 Future Enhancements:
Deploy on Render / PythonAnywhere

Add feature importance & charts

Add authentication & better UI

Streamlit version
