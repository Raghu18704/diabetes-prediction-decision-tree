

## About Project
This project predicts whether a person is diabetic using a Decision Tree classifier.
The model is designed as a **screening tool**, prioritizing high recall for diabetic patients.

## Algorithm Used
- Decision Tree Classifier
- Class imbalance handled using class weighting
- Hyperparameters tuned to balance recall and accuracy

## Dataset
- Medical attributes such as glucose level, BMI, age, etc.
- Target variable: Diabetes (0 = No, 1 = Yes)

## Model Performance
- Accuracy: 83%
- Recall (Diabetes): 95%
- Suitable for medical screening applications

## Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn