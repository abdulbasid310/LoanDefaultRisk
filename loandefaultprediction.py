# -*- coding: utf-8 -*-
"""LoanDefaultPrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ka9QFJMi7L_Xhq-BFeEPOMhrxr3ZmEx4
"""

# classification problem
# decision tree
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("Loan_default.csv")

# visuales the data
df

# Visualises data to check for NaNs
df.info()

# Store the dependent and indepedent variables in X and Y
X = df.drop(['Default','LoanID'], axis=1)
y = df['Default']
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
print(X.shape)

x_train

# Converts categorical training data into a numerical format
from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()
for i in range(9,16):
  x_train.iloc[:,i] = labelencoder_x.fit_transform(x_train.iloc[:,i])
labelencoder_y = LabelEncoder()
y_train = labelencoder_y.fit_transform(y_train)

# converts the categorical test data into a numerical format
for i in range(9,16):
  x_test.iloc[:,i] = labelencoder_x.fit_transform(x_test.iloc[:,i])
labelencoder_y = LabelEncoder()
y_test = labelencoder_y.fit_transform(y_test)

# Normalises the data
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

# Trains the classifier on the training data
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy", random_state=0)
dtc.fit(x_train, y_train)

# Gets and prints the accuracy of the decision tree classifier
from sklearn import metrics
y_pred = dtc.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Creates a dataframe for features and their importance in descending order of importance
feature_importance = dtc.feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
importance_df

# Produces a csv file of feature importance
importance_df.to_csv('feature_importance.csv', index= False)