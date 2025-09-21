# Main Flask application code
from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# --- Load the Trained Model ---
# The model is loaded only once when the app starts, for efficiency.
try:
    model = joblib.load('saved_models/RandomForest_pipeline.joblib')
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# --- Data for Dropdowns ---
# These are the exact categories the model was trained on.
MANUFACTURERS = ['Ford', 'Porsche', 'Toyota', 'VW', 'BMW']
MODELS = [
    'Fiesta', '718 Cayman', 'Mondeo', 'RAV4', 'Polo', 'Focus', 'Prius', 'Golf', 'Z4',
    'Yaris', '911', 'Passat', 'M5', 'Cayenne', 'X3'
]
FUEL_TYPES = ['Gasoline', 'Diesel', 'Hybrid', 'Electric'] # Assuming these from previous script

# --- Define Routes ---

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ""
    if request.method == 'POST':
        if not model:
            prediction_text = "Model is not available. Please check server logs."
        else:
            try:
                # --- Get Data From Form ---
                # All form data comes in as strings, so we convert types as needed.
                manufacturer = request.form.get('manufacturer')
                model_name = request.form.get('model')
                year = int(request.form.get('year'))
                mileage = int(request.form.get('mileage'))
                engine_size = float(request.form.get('engine_size'))
                fuel_type = request.form.get('fuel_type')

                # --- Feature Engineering ---
                # We must create the 'Age' feature, just like in training.
                age = 2024 - year

                # --- Create DataFrame for Prediction ---
                # The column order and names must EXACTLY match the training data.
                input_data = pd.DataFrame({
                    'Manufacturer': [manufacturer],
                    'Model': [model_name],
                    'Engine size': [engine_size],
                    'Fuel type': [fuel_type],
                    'Mileage': [mileage],
                    'Age': [age]
                })

                print("Input Data for Prediction:\n", input_data)

                # --- Make Prediction ---
                prediction = model.predict(input_data)
                predicted_price = prediction[0]

                # --- Format Output ---
                prediction_text = f"Predicted Price: ${predicted_price:,.2f}"

            except Exception as e:
                prediction_text = f"An error occurred: {e}"

    # On a GET request or after a POST, render the page.
    # Pass the dropdown data and the prediction result to the template.
    return render_template(
        'index.html',
        manufacturers=MANUFACTURERS,
        models=MODELS,
        fuel_types=FUEL_TYPES,
        prediction_text=prediction_text
    )

if __name__ == '__main__':
    # Runs the app on a local development server.
    app.run(debug=True)