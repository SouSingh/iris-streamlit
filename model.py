import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from xgboost import XGBClassifier

iris = pd.read_csv("Iris.csv")
iris['Species'].unique()
iris['Species'] = iris['Species'].replace(['Iris-setosa','Iris-versicolor','Iris-virginica'],[0,1,2])
X = iris.drop(['Id','Species'], axis = 1)
Y = iris['Species']
X_train,X_test,y_train,y_test = train_test_split(X, Y, test_size=0.20, random_state=42)
model = XGBClassifier(n_estimators = 400, learning_rate = 0.1, max_depth = 3)
model.fit(X_train, y_train)

def output(q1,q2,q3,q4):
    data = [[q1,q2,q3,q4]]
    df = pd.DataFrame(data,columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
    return model.predict(df)