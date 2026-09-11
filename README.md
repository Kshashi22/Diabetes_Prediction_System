# Diabetes Prediction System

A machine learning-powered web application that predicts the likelihood of diabetes based on patient health and medical attributes.

The project combines **data preprocessing, exploratory data analysis, machine learning, and web deployment** into an end-to-end healthcare analytics solution.

## Live Demo

[Live Application](https://diabetes-prediction-system-theta.vercel.app/)

## GitHub Repository

[View Source Code](https://github.com/Kshashi22/Diabetes_Prediction_System)

---

## Overview

Diabetes is one of the most common chronic health conditions worldwide. Early identification of potential diabetes risk can support timely medical attention and better health management.

This project uses a trained machine learning classification model to analyze patient information and generate a diabetes prediction.

Users can enter the following health parameters:

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

The application processes these inputs through the trained machine learning model and returns a prediction.

> **Disclaimer:** This application is developed for educational and research purposes. It is not intended to provide medical diagnosis, treatment recommendations, or professional healthcare advice.

---

## Key Features

* Machine learning-based diabetes prediction
* Interactive web interface
* Eight healthcare-related input parameters
* Data preprocessing and analysis
* Classification-based prediction
* Trained ML model integration
* Web-based prediction workflow
* Deployed and accessible online
* Clean and simple user interface
* Repository includes the complete development workflow

---

## Machine Learning Workflow

The project follows an end-to-end machine learning pipeline:

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning & Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Prediction
     ↓
Web Application
```

---

## Dataset

The project uses a diabetes dataset containing medical and demographic attributes.

### Features

| Feature                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| Pregnancies                | Number of pregnancies                         |
| Glucose                    | Plasma glucose concentration                  |
| Blood Pressure             | Diastolic blood pressure                      |
| Skin Thickness             | Skin fold thickness                           |
| Insulin                    | Serum insulin level                           |
| BMI                        | Body Mass Index                               |
| Diabetes Pedigree Function | A measure related to hereditary diabetes risk |
| Age                        | Age of the patient                            |
| Outcome                    | Target variable indicating diabetes status    |

### Target Variable

```text
0 → No Diabetes
1 → Diabetes
```

---

## Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Web Development

* HTML
* CSS
* JavaScript
* Flask

### Deployment

* Vercel

### Development Tools

* Jupyter Notebook
* Google Colab
* VS Code
* Git
* GitHub

---

## Exploratory Data Analysis

The project includes exploratory analysis to understand patterns and relationships within the dataset.

The analysis focuses on:

* Distribution of diabetes outcomes
* Glucose-level patterns
* BMI distribution
* Age distribution
* Blood pressure patterns
* Insulin levels
* Correlation between features
* Feature relationships
* Data distributions and potential outliers

Visualization techniques include:

* Histograms
* Box plots
* Count plots
* Scatter plots
* Correlation heatmaps
* Distribution plots

---

## Model Development

The machine learning component treats diabetes prediction as a **binary classification problem**.

The workflow includes:

1. Loading the dataset
2. Understanding the data
3. Checking data quality
4. Performing preprocessing
5. Separating features and target
6. Splitting data into training and testing sets
7. Training the classification model
8. Evaluating model performance
9. Integrating the trained model with the web application

The final model is used to generate predictions from new patient inputs.

---

## Web Application

The web application provides a simple interface where users can enter patient information and request a prediction.

### Prediction Flow

```text
User Input
    ↓
Health Parameters
    ↓
Data Processing
    ↓
Trained ML Model
    ↓
Prediction
    ↓
Result
```

The deployed application is available here:

**[Open Diabetes Prediction System](https://diabetes-prediction-system-theta.vercel.app/)**

---

## Project Structure

```text
Diabetes_Prediction_System/
│
├── api/
│   └── ...
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
├── Diabetic.ipynb
├── app.py
├── requirements.txt
├── vercel.json
├── HOW_TO_USE.md
└── README.md
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kshashi22/Diabetes_Prediction_System.git
```

### 2. Navigate to the Project Directory

```bash
cd Diabetes_Prediction_System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open the local application in your browser using the URL displayed by Flask.

---

## Using the Application

1. Open the web application.
2. Enter the patient's health information.
3. Provide values for all required parameters.
4. Click **Predict**.
5. The trained machine learning model processes the input.
6. The application displays the prediction result.

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Python programming
* Data cleaning
* Exploratory Data Analysis
* Data visualization
* Feature analysis
* Machine learning
* Classification
* Model evaluation
* Healthcare analytics
* Flask application development
* API integration
* Web development
* Git and GitHub
* Cloud deployment

---

## Future Improvements

Potential improvements include:

* Comparing multiple machine learning algorithms
* Hyperparameter tuning
* Cross-validation
* Feature engineering
* Improved handling of missing and invalid values
* Class imbalance handling
* Model explainability using SHAP
* Probability-based risk scoring
* Improved UI/UX
* Interactive data visualization
* Prediction history
* Healthcare analytics dashboard
* Model performance monitoring
* Containerization using Docker

---

## Important Note

This project is intended strictly for **educational, research, and demonstration purposes**.

The prediction generated by this system should not be considered a medical diagnosis. Users should consult qualified healthcare professionals for medical advice, diagnosis, or treatment.

---

## Author

### Kanishka Shashi

Computer Science undergraduate specializing in **Artificial Intelligence & Machine Learning**, with interests in Data Analytics, Machine Learning, Full-Stack Development, and Generative AI.

### Connect With Me

* GitHub: [Kshashi22](https://github.com/Kshashi22)
* LinkedIn: [Kanishka Shashi](https://www.linkedin.com/in/kanishka-shashi-5390252a1/)

---

## Project Links

* **Live Demo:** https://diabetes-prediction-system-theta.vercel.app/
* **GitHub:** https://github.com/Kshashi22/Diabetes_Prediction_System

---

## Support

If you found this project useful or interesting, consider giving the repository a **star** on GitHub.

Feedback, suggestions, and contributions are always welcome.
