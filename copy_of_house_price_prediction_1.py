# -*- coding: utf-8 -*-
"""Copy of House Price Prediction .1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_vrECGwze79YvQZOPoEmiH3p27Q8mlgZ
"""

# Commented out IPython magic to ensure Python compatibility.
variable_name = "" # @param {type:"string"}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error,r2_score
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
# %matplotlib inline

data=pd.read_csv('/content/house_data.csv')
data

data.head()

data.info()

data.duplicated().sum()

data.bathrooms.value_counts()

data.shape

data.columns

data.drop(columns=['id' , 'date' , 'zipcode'] , inplace=True)
data.head()

data.bathrooms.value_counts().plot(kind='bar')

sns.countplot(data=data,x='grade')

data.waterfront.value_counts()

data.waterfront.value_counts().reset_index().plot(kind='bar')

data.view.value_counts()

data.view.value_counts().reset_index()

data.view.value_counts().reset_index().plot(kind='bar')

plt.figure(figsize=(10, 10))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

sns.lineplot(data=data,x='bedrooms',y='price')

#define the feature  x abd y
x=data.drop(columns=['price'])
y=data.price

scaler=StandardScaler()
x=scaler.fit_transform(x)
y=scaler.fit_transform(y.values.reshape(-1,1))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,shuffle=True, random_state=20)

lr=LinearRegression()
lr.fit(x_train,y_train)

lr.score(x_train,y_train)

y_predict=lr.predict(x_test)

print(r2_score(y_predict,y_test))

ls=Lasso(max_iter=10000,alpha=.0001)
ls.fit(x_train,y_train)

ls.score(x_train,y_train)

y_predict=ls.predict(x_test)

print(r2_score(y_predict,y_test))

ds_model=DecisionTreeRegressor()
ds_model.fit(x_train,y_train)

ds_model.score(x_train,y_train)

y_predict=ds_model.predict(x_test)

print(r2_score(y_predict,y_test))

rf_reg= RandomForestRegressor(n_estimators=500)
rf_reg.fit(x_train,y_train)

rf_reg.score(x_train,y_train)

y_predict=rf_reg.predict(x_test)

print(r2_score(y_predict,y_test))

svr = SVR(gamma='scale' , C=5)
svr.fit(x_train , y_train)

svr.score(x_train,y_train)

y_predict=svr.predict(x_test)

print(r2_score(y_test,y_predict))