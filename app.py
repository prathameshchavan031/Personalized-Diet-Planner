from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and feature names
with open('model/diet_model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    model = model_data['model']
    feature_names = model_data['feature_names']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = request.form['gender']
    bmi = float(request.form['bmi'])
    health = request.form['health']
    allergy = request.form['allergy']
    preference = request.form['preference']

    # Convert categorical values manually (same order as training)
    gender_map = {'Male': 0, 'Female': 1}
    health_map = {'None': 0, 'Diabetes': 1, 'BP': 2}
    allergy_map = {'None': 0, 'Milk': 1, 'Nuts': 2}
    preference_map = {'Veg': 0, 'Non-Veg': 1}

    input_data = np.array([[age,
                            gender_map[gender],
                            bmi,
                            health_map[health],
                            allergy_map[allergy],
                            preference_map[preference]]])

    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Recommended Diet: {prediction}')

if __name__ == '__main__':
    app.run(debug=True)
