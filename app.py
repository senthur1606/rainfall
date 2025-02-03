from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests

# Load the trained model
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Get input data from request
        input_df = pd.DataFrame([data], columns=feature_names)  # Convert to DataFrame
        prediction = model.predict(input_df)[0]  # Make prediction
        return jsonify({"prediction": int(prediction)})  # Return result as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error message if any

if __name__ == "__main__":
    app.run(debug=True)
