"""Week 3 - Task 5: Student Performance Prediction (Pass/Fail) using Logistic Regression."""


# # Week 3 - Task 5: Mini Project - Student Performance Prediction
# **Goal:** predict whether a student will **Pass or Fail** from Study Hours, Attendance, Previous Marks and Assignment Score using a Machine Learning classification model (Logistic Regression).


# ## 1. Load the dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width', 120); pd.set_option('display.max_columns', 20)

df = pd.read_csv("Dataset.csv")
print("Shape:", df.shape)
df.head()


# ## 2. Clean the data

print("Missing values:", df.isnull().sum().sum(), "| Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()                                   # remove duplicate records
num_cols = ["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score"]
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())              # fill missing values with median
df = df.reset_index(drop=True)

print("After cleaning -> Missing:", df.isnull().sum().sum(), "| Duplicates:", df.duplicated().sum(), "| Shape:", df.shape)
print()
print(df["Result"].value_counts())

counts = df["Result"].value_counts()
plt.figure(figsize=(4.8, 3.4))
bars = plt.bar(counts.index, counts.values, color=["#7bc67e", "#e57373"])
plt.bar_label(bars)
plt.title("Pass vs Fail in the Dataset"); plt.ylabel("Students")
plt.show()


# ## 3. Select features and target

features = ["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score"]
X = df[features]
y = df["Result"]
print("Features:", features)
print("Target  : Result (Pass / Fail)")


# ## 4. Split into training and testing data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Training records:", len(X_train), "| Testing records:", len(X_test))


# ## 5. Train a classification model

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_s, y_train)
print("Logistic Regression model trained")


# ## 6. Make predictions and calculate accuracy

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

y_pred = model.predict(X_test_s)
print("Model Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print()
print("Confusion matrix [Fail, Pass]:")
print(confusion_matrix(y_test, y_pred, labels=["Fail", "Pass"]))
print()
print(classification_report(y_test, y_pred))

# Comparison with a second model (Decision Tree) to check that the result is reasonable
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print("Decision Tree accuracy      :", round(accuracy_score(y_test, tree.predict(X_test)) * 100, 2), "%")
print("Logistic Regression accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

coef = pd.Series(model.coef_[0], index=features).sort_values()
plt.figure(figsize=(5.5, 3.4))
plt.barh(coef.index, coef.values, color="#4f8ef7")
plt.title("Importance of Each Feature (coefficients)"); plt.xlabel("Coefficient")
plt.show()


# ## 7. Test the model with new student inputs

def predict_student(study_hours, attendance, previous_marks, assignment_score):
    """Predict Pass/Fail for a new student."""
    student = pd.DataFrame([[study_hours, attendance, previous_marks, assignment_score]], columns=features)
    scaled = scaler.transform(student)
    result = model.predict(scaled)[0]
    p_pass = model.predict_proba(scaled)[0][list(model.classes_).index("Pass")]
    print(f"Study Hours: {study_hours} | Attendance: {attendance}% | Previous Marks: {previous_marks} | Assignment: {assignment_score}")
    print(f"Prediction: {result.upper()}  (probability of passing = {p_pass:.2f})\n")

predict_student(6, 85, 72, 70)    # strong student
predict_student(2, 55, 40, 35)    # weak student
predict_student(4, 70, 55, 60)    # average student
predict_student(8, 90, 80, 85)    # very hardworking student

# Try your own input
hours = float(input("Study hours per day: "))
att = float(input("Attendance %: "))
prev = float(input("Previous marks: "))
assign = float(input("Assignment score: "))
predict_student(hours, att, prev, assign)


# ## 8. Project Report
# **Dataset used:** A student performance dataset (`Dataset.csv`) with 204 records. After removing 4 duplicate rows and filling 21 missing values with the median, 200 students remained. About 72% of them passed.
#
# **Features selected:** Study Hours, Attendance, Previous Marks and Assignment Score. The target is `Result` (Pass/Fail). Student ID was ignored because it is only an identifier.
#
# **Model used:** Logistic Regression, a classification algorithm that outputs the probability of passing. The data was split 80/20 (160 training, 40 testing records) and the features were scaled with StandardScaler.
#
# **Results and accuracy:** The model reached **90% accuracy** on the test data, correctly predicting 36 of 40 students. It found 28 of 29 passing students but only 8 of 11 failing students. A Decision Tree gave 85%, so Logistic Regression was kept. For new students it predicted PASS for (6 hrs, 85%, 72 marks, 70 assignment) and FAIL for (2 hrs, 55%, 40 marks, 35 assignment).
#
# **Limitations:** The dataset is small and was prepared for practice, so real results may differ. The test set has only 40 students, so accuracy can change with a different split. Fewer failing students means weaker detection of "Fail", and only four features are used.
#
# **Future improvements:** Use a larger real dataset, add features such as class participation, use cross-validation, handle class imbalance, compare Random Forest, and build a small web app for predictions.
