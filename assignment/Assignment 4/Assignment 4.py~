#Load dependencies in python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.datasets import load_iris

#Load Iris Dataset
iris=load_iris()
for keys in iris.keys() :
    print(keys)

#Define X and y from dataset and split the dataset in test and train    
X=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)


#Print test and train
print('X_train')
print(X_train)
print('X_test')
print(X_test)

#Import dependencies for Classifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Display the accuracy
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc.score(X_test, y_test)
