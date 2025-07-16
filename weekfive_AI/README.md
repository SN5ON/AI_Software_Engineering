# Diabetes Readmission Prediction

## Project Overview

This project aims to predict whether a patient with diabetes will be readmitted to the hospital within 30 days, based on their medical and demographic data. The prediction task is a binary classification problem with imbalanced classes.

---

## Data Preparation

- Loaded the dataset and cleaned missing or irrelevant data.
- Handled missing values in categorical and numerical features.
- Identified features:
  - Numerical features: 11
  - Categorical features: 33
- Encoded categorical features using OneHotEncoder.
- Standardized numerical features using StandardScaler.
- Split the data into training and testing sets.

---

## Modeling

### Baseline Logistic Regression

- Trained a logistic regression model without class weights.
- Observed high accuracy (~88%) but poor recall for the positive class (readmission).

### Weighted Logistic Regression

- Applied `class_weight='balanced'` to address class imbalance.
- Created a pipeline combining preprocessing and logistic regression.
- Trained and evaluated the weighted logistic regression model.

---

## Results

Confusion Matrix (Weighted Logistic Regression):
[[11882 6201]
[ 1024 1247]]

Classification Report:

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.92      | 0.66   | 0.77     | 18083   |
| 1     | 0.17      | 0.55   | 0.26     | 2271    |

- Accuracy: 65%
- Macro avg recall: 60%
- Weighted avg F1-score: 71%

The weighted logistic regression model improves recall on the minority class but at some cost to precision and overall accuracy.

---

## Future Work

- Implement SMOTE or other resampling techniques.
- Experiment with advanced models: Random Forest, XGBoost.
- Perform hyperparameter tuning.
- Develop and deploy an interactive Streamlit web app for model inference.

---

## Environment & Dependencies

- Python 3.x
- Libraries:
  - pandas
  - scikit-learn
  - joblib
  - streamlit (for deployment)
- Development performed in Google Colab.

---

## Usage 
Deployment will be added as a Streamlit app in future updates.

---
