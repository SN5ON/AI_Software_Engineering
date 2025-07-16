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
Assignment: Understanding the AI Development Workflow
Course: AI for Software Engineering
Duration: 7 days
Total Points: 100

Objective & Guidelines

This assignment tests your ability to apply the AI Development Workflow to a real-world problem. You will demonstrate understanding of key stages—from problem definition to deployment—and critically analyze challenges and ethical considerations.

The assignment should be handled in peer groups. 

Submission Guidelines

PDF, 5–10 pages (excluding diagrams). Include section headings and references.

GitHub Repository with all codes well commented. 

Share the PDF as an article in the PLP Academy Community .

Grading Rubric

Completeness: All sections addressed (30%).

Accuracy: Technical correctness (40%).

Critical Analysis: Depth of ethical and practical insights (20%).

Clarity: Organization and presentation (10%).

Part 1: Short Answer Questions (30 points)

1. Problem Definition (6 points)

Define a hypothetical AI problem (e.g., "Predicting student dropout rates").

List 3 objectives and 2 stakeholders.

Propose 1 Key Performance Indicator (KPI) to measure success.

2. Data Collection & Preprocessing (8 points)

Identify 2 data sources for your problem.

Explain 1 potential bias in the data.

Outline 3 preprocessing steps (e.g., handling missing data, normalization).

3. Model Development (8 points)

Choose a model (e.g., Random Forest, Neural Network) and justify your choice.

Describe how you would split data into training/validation/test sets.

Name 2 hyperparameters you would tune and why.

4. Evaluation & Deployment (8 points)

Select 2 evaluation metrics and explain their relevance.

What is concept drift? How would you monitor it post-deployment?

Describe 1 technical challenge during deployment (e.g., scalability).

Part 2: Case Study Application (40 points)

Scenario: A hospital wants an AI system to predict patient readmission risk within 30 days of discharge.

Tasks:

Problem Scope (5 points): Define the problem, objectives, and stakeholders.

Data Strategy (10 points):

Propose data sources (e.g., EHRs, demographics).

Identify 2 ethical concerns (e.g., patient privacy).

Design a preprocessing pipeline (include feature engineering steps).

Model Development (10 points):

Select a model and justify it.

Create a confusion matrix and calculate precision/recall (hypothetical data).

Deployment (10 points):

Outline steps to integrate the model into the hospital’s system.

How would you ensure compliance with healthcare regulations (e.g., HIPAA)?

Optimization (5 points): Propose 1 method to address overfitting.

Part 3: Critical Thinking (20 points)

Ethics & Bias (10 points):

How might biased training data affect patient outcomes in the case study?

Suggest 1 strategy to mitigate this bias.

Trade-offs (10 points):

Discuss the trade-off between model interpretability and accuracy in healthcare.

If the hospital has limited computational resources, how might this impact model choice?

Part 4: Reflection & Workflow Diagram (10 points)

Reflection (5 points):

What was the most challenging part of the workflow? Why?

How would you improve your approach with more time/resources?

Diagram (5 points):

Sketch a flowchart of the AI Development Workflow, labeling all stages.

Tip: Review lecture notes on preprocessing, evaluation metrics, and the CRISP-DM framework.

This assignment encourages holistic thinking about AI projects while emphasizing ethics and real-world constraints. Good luck! 🚀