import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# loading points data for all matches
ml_data = pickle.load(open("final_ml_data.dat", "rb"))
# ml_data.shape
ml_data.dropna(axis=0, inplace=True)
# ml_data.shape
# ml_data.info()
ml_data.drop(["pbp_id", "player_1", 'player_2', 'winner'], axis=1, inplace=True)

y = ml_data['point_winner']
X = ml_data.drop(["point_winner"], axis=1)
del(ml_data)

# splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# y_train = ml_data['point_winner']
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.fit_transform(y_test)

# Using Column Transformer
# https://scikit-learn.org/stable/modules/compose.html#columntransformer-for-heterogeneous-data
column_trans = make_column_transformer(
    (OneHotEncoder(), [1]+list(range(4, 24))),
    remainder='passthrough')
column_trans.fit(X_train)
# column_trans.get_feature_names()
X_train = column_trans.transform(X_train)
X_test = column_trans.transform(X_test)

# -----------------------------------------------------------------------------------
# Fitting a basic Logistic Regression estimator
clf_LogReg = LogisticRegression()
clf_LogReg.fit(X_train, y_train)

# checking predictions on training data itself
# temp = len(X_train)
# prediction = pd.DataFrame(clf_LogReg.predict(X_train[1:temp,:]), columns=['Predicted'])
# prediction['Actual'] = y_train[1:temp]
# prediction['Correct Prediction'] = prediction['Predicted']==prediction['Actual']
# print(f"Predicted percent is: {sum(prediction['Correct Prediction'])/len(prediction)*100}%")
# or alternatively, just use the score function

# clf_LogReg.score(X_train, y_train)

# checking predictions on test data
# clf_LogReg.score(X_test, y_test)

# -----------------------------------------------------------------------------------
# Fitting a decision tree
clf_DecTree = DecisionTreeClassifier(random_state=42)
clf_DecTree.fit(X_train, y_train)
# checking predictions on training data itself
clf_DecTree.score(X_train, y_train)
# checking predictions on test data
clf_DecTree.score(X_test, y_test)

# -----------------------------------------------------------------------------------
# Fitting a random forest
clf_RanFor = RandomForestClassifier(n_estimators=100,
                               random_state=42,
                               max_features='sqrt', njobs=-1, verbose=1)
clf_RanFor.fit(X_train, y_train)
# checking predictions on training data itself
clf_RanFor.score(X_train, y_train)
# checking predictions on test data
clf_RanFor.score(X_test, y_test)

# Creating the confusion matrix
expected = y_test
predicted = clf_RanFor.predict(X_test)
results = confusion_matrix(expected, predicted)
print(results)






