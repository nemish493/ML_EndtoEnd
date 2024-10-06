import pickle
from flask import Flask ,request ,render_template, jsonify,app,url_for

import numpy as np
import pandas as pd

app = Flask(__name__)
knnmodel = pickle.load(open('knn.pkl', 'rb'))
robust_scaler = pickle.load(open('robust_scaler.pkl', 'rb'))
standard_scaler_temp_ph = pickle.load(open('standard_scaler_temp_ph.pkl', 'rb'))
final_scaler = pickle.load(open('final_scaler.pkl', 'rb'))

NPK_cols = ['N', 'P', 'K']
temp_ph_cols = ['temperature', 'ph']
rainfall_humidity_cols = ['rainfall', 'humidity']

# Function to preprocess the input data
def preprocess_input(data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([data], columns=NPK_cols + temp_ph_cols + rainfall_humidity_cols)
    
    # Apply RobustScaler to N, P, K
    input_df[NPK_cols] = robust_scaler.transform(input_df[NPK_cols])
    
    # Apply StandardScaler to temperature and ph
    input_df[temp_ph_cols] = standard_scaler_temp_ph.transform(input_df[temp_ph_cols])
    
    # Apply log transformation to rainfall and humidity
    input_df[rainfall_humidity_cols] = np.log1p(input_df[rainfall_humidity_cols])
    
    # Combine the transformed features and apply the final scaler
    combined_features = input_df[NPK_cols + temp_ph_cols + rainfall_humidity_cols]
    final_scaled_data = final_scaler.transform(combined_features)
    
    return final_scaled_data

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    
    # Preprocess the input data
    preprocessed_data = preprocess_input(data)
    
    # Make prediction using the preprocessed data
    output = knnmodel.predict(preprocessed_data)
    print(output[0])
    print(preprocessed_data)
    
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    # Convert form data to a dictionary
    data = {col: float(value) for col, value in zip(NPK_cols + temp_ph_cols + rainfall_humidity_cols, request.form.values())}
    
    # Preprocess the input data
    preprocessed_data = preprocess_input(data)
    
    # Make prediction using the preprocessed data
    output = knnmodel.predict(preprocessed_data)
    print(output[0])
    print(data)
    
    return render_template('home.html', prediction_text=f'this is the predicted crop  { output[0] }')

if __name__ == '__main__':
    app.run(debug=True)
