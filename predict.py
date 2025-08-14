import pickle
from flask import Flask, request, jsonify
import pandas as pd
 
# Load the trained model
with open('lr_model.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    
def prepare_features(ride):
    return pd.DataFrame([{
        'cylinders': ride['cylinders'],
        'displacement': ride['displacement'],
        'weight': ride['weight'],
        'acceleration': ride['acceleration']
    }])
 
def predict(features_df):
    preds = model.predict(features_df)
    return float(preds[0])
 
app = Flask('mpg-prediction')
 
@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()
 
    features_df = prepare_features(ride)
    pred = predict(features_df)
 
    result = {
        'predicted_mpg': pred
    }
 
    return jsonify(result)
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
 
 