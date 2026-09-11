import os
from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np

# Resolve paths 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "static", "diabetes_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "static", "scaler.pkl")

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

#  Check model classes to understand label encoding
try:
    if hasattr(model, 'classes_'):
        print(f"Model classes: {model.classes_}")
    if hasattr(model, 'classes'):
        print(f"Model classes: {model.classes}")
except:
    pass

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    input_data = None
    
    if request.method == 'POST':
        # Get data from form
        preg = float(request.form['pregnancies'])
        gluc = float(request.form['glucose'])
        bp = float(request.form['bp'])
        skin = float(request.form['skin'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = float(request.form['age'])

        # Store input data
        input_data = {
            'pregnancies': preg,
            'glucose': gluc,
            'bp': bp,
            'skin': skin,
            'insulin': insulin,
            'bmi': bmi,
            'dpf': dpf,
            'age': age
        }

        # Create array and scale
        user_data = np.array([[preg, gluc, bp, skin, insulin, bmi, dpf, age]])
        user_data_scaled = scaler.transform(user_data)

        
        try:
            # Get probability predictions
            pred_proba = model.predict_proba(user_data_scaled)[0]
            
            # Check model classes to determine which index corresponds to diabetes
            if hasattr(model, 'classes_'):
                classes = model.classes_
                # Find which class index corresponds to diabetes
                #  classes[0] = 0 (no diabetes), classes[1] = 1 (diabetes)
                # But check actual class values
                if len(classes) == 2:
                    # If classes are [0, 1], then index 1 is diabetes
                    # If classes are [1, 0], then index 0 is diabetes
                    if classes[0] == 0 and classes[1] == 1:
                        prob_diabetes = pred_proba[1] 
                    elif classes[0] == 1 and classes[1] == 0:
                        prob_diabetes = pred_proba[0]  
                    else:
                        # Try to find class 1
                        diabetes_class_idx = np.where(classes == 1)[0]
                        if len(diabetes_class_idx) > 0:
                            prob_diabetes = pred_proba[diabetes_class_idx[0]]
                        else:
                            prob_diabetes = pred_proba[1] 
                else:
                    prob_diabetes = pred_proba[1] 
            else:
                # Default assumption: [prob_no_diabetes, prob_diabetes]
                prob_diabetes = pred_proba[1]
            
            has_diabetes = prob_diabetes >= 0.5
            
          
            print(f"Prediction probabilities: {pred_proba}, Prob diabetes: {prob_diabetes:.4f}, Prediction: {'Diabetes' if has_diabetes else 'No Diabetes'}")
        except (AttributeError, IndexError) as e:
            # Fallback to regular predict if predict_proba not available
            pred = model.predict(user_data_scaled)
            pred_value = pred[0]
            
        
            print(f"Raw prediction value: {pred_value}, type: {type(pred_value)}, error: {e}")
            
            # Convert boolean to int if needed
            if isinstance(pred_value, (bool, np.bool_)):
                pred_value = int(pred_value)
            
        
            if hasattr(model, 'classes_'):
                classes = model.classes_
                # If classes are [0, 1]: 1 = diabetes, 0 = no diabetes (standard)
                # If classes are [1, 0]: 0 = diabetes, 1 = no diabetes (reversed)
                if len(classes) == 2:
                    if classes[0] == 1 and classes[1] == 0:
                        # Reversed labels: 0 = diabetes, 1 = no diabetes
                        has_diabetes = (pred_value == 0)
                    else:
                        # Standard labels: 1 = diabetes, 0 = no diabetes
                        has_diabetes = (pred_value == 1)
                else:
                    # Default: 1 = diabetes, 0 = no diabetes
                    has_diabetes = (pred_value == 1) or (pred_value == True)
            else:
                # Default assumption: 1 = diabetes, 0 = no diabetes
                has_diabetes = (pred_value == 1) or (pred_value == True)
            
            print(f"Binary prediction: {pred_value}, interpreted as: {'Diabetes' if has_diabetes else 'No Diabetes'}")
        
        if has_diabetes:
            session['prediction'] = "The person is likely to have diabetes."
        else:
            session['prediction'] = "The person is not likely to have diabetes."
        
        session['input_data'] = input_data
        return redirect(url_for('index'))
    
    # Get prediction and input data from 
    if 'prediction' in session:
        prediction = session.pop('prediction')
    if 'input_data' in session:
        input_data = session.pop('input_data')

    return render_template('index.html', prediction=prediction, input_data=input_data)

if __name__ == "__main__":
    app.run(debug=True)

