# Diabetic_Prediction_System

🩺 Diabetes Prediction System using Machine Learning

A Machine Learning–based web-ready diabetes prediction system built using Logistic Regression.
This project predicts whether a person is likely to have diabetes based on medical attributes.

📌 Project Overview

Early detection of diabetes can help in effective treatment and lifestyle management.
This system uses a supervised learning approach to predict diabetes using patient health data.

The model is trained on the PIMA Indians Diabetes Dataset and achieves reliable prediction accuracy using feature scaling and logistic regression.

🚀 Features

✅ Data preprocessing and correlation analysis

✅ Feature scaling using StandardScaler

✅ Logistic Regression model training

✅ Model evaluation (Accuracy, Confusion Matrix, Classification Report)

✅ User input–based prediction

✅ Saved trained model and scaler (.pkl files)

✅ Ready for web app integration (Flask)

📊 Dataset Details

Dataset: PIMA Indians Diabetes Dataset

Input Features:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

Target Variable:

Outcome


1 → Diabetic

0 → Not Diabetic

🧠 Machine Learning Model

Algorithm: Logistic Regression
Feature Scaling: StandardScaler
Train-Test Split: 80% Training / 20% Testing
Accuracy: ~75%

🧪 Model Evaluation

Accuracy Score
Confusion Matrix
Precision, Recall, F1-score

🛠️ Technologies Used

Python
Pandas & NumPy
Matplotlib & Seaborn
Scikit-learn
Jupyter Notebook
Joblib


A person with no diabetc
<img width="1919" height="947" alt="image" src="https://github.com/user-attachments/assets/069b2601-060c-46e4-ae79-0d5c823033bb" />

A person with diabetic
<img width="1913" height="966" alt="image" src="https://github.com/user-attachments/assets/017e6dcf-2e10-4da0-bcf1-dae1bbcd0650" />


▶️ How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/Osagani31/Diabetes-Prediction-System.git

cd Diabetes-Prediction-System

2️⃣ Install Required Libraries

pip install numpy pandas matplotlib seaborn scikit-learn joblib

3️⃣ Run Jupyter Notebook

jupyter notebook


Open diabetes_prediction.ipynb and run all cells.

🧪 Sample Prediction

new_data = [[2, 120, 70, 20, 79, 25.5, 0.5, 33]]

prediction = model.predict(scaler.transform(new_data))

Output:

The person is not likely to have diabetes.
