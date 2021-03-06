# -*- coding: utf-8 -*-
"""car_price_prediction(project).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oMd1WGxe6YkSVI1VEyJaVMFR68GqYzKq

**Objective Of Car Price Prediction Project:** 

For this project we are using a car dataset, where we want to predict the selling price of car based on its certain features. Since we need to find the real value, with real calculation, therefore this problem is regression problem. We will be using regression machine learning algorithms to solve this problem.
"""

## Loading Required Libraries ##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

"""<h2> <b> Data Gathering : </b> </h2>"""

df = pd.read_csv('/content/car data.csv')

"""<h2> <b> Data Preparation: </b> </h2>"""

# check datatypes of columns
df.info()

df.shape    #It will tell number of rows and columns

#statistical Summary
df.describe()

"""**Note :** In this dataset , we have 4 columns of object datatpe . Out of that 4 , 3 are categorical and one is non categorical. We need to remove non-categorical type (means Car_Name).
We will do it later.
"""

df.isnull().sum()

"""We don't have any null value anywhere...

<h2> <b> Feature Engineering </b></h2>
"""

#Adding a column current_year in dataframe
df['Current_Year']=2021
df.head()

# Adding a column which contain the no of year car used 
df['Car_Age'] = df['Current_Year'] - df['Year']
df.head()

# Remove the column Car_Name ,current_year,Year
df.drop(columns=['Year','Car_Name','Current_Year'],inplace=True,axis=1)
df.head()

#change categorical object datatype in numerical data type using 'get_dummies' function
df = pd.get_dummies(df,columns=['Fuel_Type','Seller_Type','Transmission'],drop_first=True)
df.head()

"""**PairPlot**"""

# To see the pairwise relationship of our dataset 
sns.pairplot(df)

"""**Heatmap**"""

correlation = df.corr()
index = correlation.index    #index contain the column name
plt.figure(figsize=(26,22))  #set height and width for clear visualization
#annot = True , dsiplays text over the cells.
#cmap = "YlGnBu" is nothing but adjustment of colors for our heatmap
sns.heatmap(correlation,annot=True,cmap='YlGnBu')

"""We are not doing Exploratory data Analysis here, focussing on creating machine learning model.
We can see EDA from here : 
https://www.analyticsvidhya.com/blog/2020/08/exploratory-data-analysiseda-from-scratch-in-python/

<h2> <b>Feature and Target Variable</b></h2>
"""

X = df.iloc[: ,1:] 
Y = df.iloc[:,0]   #taking selling price as target variable

"""<h2> <b> Feature Importance </b> </h2>

"""

#checking and comparing the importance of features
from sklearn.ensemble import ExtraTreesRegressor
#creating object
mod = ExtraTreesRegressor()
#fitting model
mod.fit(X,Y)

print(mod.feature_importances_)

#plot graph of feature importances for better visualization
feature_imp = pd.Series(mod.feature_importances_,index = X.columns)
print(feature_imp)
# considering top 5 important features
feature_imp.nlargest(5).plot(kind='barh')
plt.show()

"""<h2> <b> Splitting data into training and testing dataset </b> </h2>"""

from sklearn.model_selection import train_test_split
X_train,X_test, Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state =1)

"""<h2> <b> Fitting and evaluating different models </b> </h2>
Here, we are using 3 different regression technique:

1 Linear regression
2 Decision Tree
3 Random Forest Regressor

We will choose one from these 3 regression technique having better accuracy.

<h2> <b> Linear Regression Model </b> </h2>
"""

from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(X_train,Y_train)  # Training the model
Y_predict = model1.predict(X_test)

#calculating model score and error
#since this is a regression technique, we can't use accuracy score.. we can use R2 score or normal score
print(model1.score(X_test, Y_test))

from sklearn import metrics
R2 = metrics.r2_score(Y_test,Y_predict)
print('R2 :' , R2)

#mean absolute error
print('MAE:', metrics.mean_absolute_error(Y_test, Y_predict))

#print mean squared error
print('MSE:', metrics.mean_squared_error(Y_test, Y_predict))

#print root mean squared error
print('MSE:', np.sqrt(metrics.mean_squared_error(Y_test, Y_predict)))

"""<h2> <b> Decision Tree Model </b> </h2>"""

from sklearn.tree import DecisionTreeRegressor

#creating object
tree = DecisionTreeRegressor()

#model fitting
tree.fit(X_train,Y_train)

Y_predict = tree.predict(X_test)

from sklearn import metrics
R2 = metrics.r2_score(Y_test,Y_predict)
print('R2 :' , R2)

#mean absolute error
print('MAE:', metrics.mean_absolute_error(Y_test, Y_predict))

#print mean squared error
print('MSE:', metrics.mean_squared_error(Y_test, Y_predict))

#print root mean squared error
print('MSE:', np.sqrt(metrics.mean_squared_error(Y_test, Y_predict)))

"""<h2> <b> Random Forest Model </b> </h2>"""

from sklearn.ensemble import RandomForestRegressor

#creating object
rf = RandomForestRegressor(n_estimators = 50, random_state = 1)

#fitting model
rf.fit(X_train,Y_train)

y_predict = rf.predict(X_test)

from sklearn import metrics
R2 = metrics.r2_score(Y_test,Y_predict)
print('R2 :' , R2)

#mean absolute error
print('MAE:', metrics.mean_absolute_error(Y_test, Y_predict))

#print mean squared error
print('MSE:', metrics.mean_squared_error(Y_test, Y_predict))

#print root mean squared error
print('MSE:', np.sqrt(metrics.mean_squared_error(Y_test, Y_predict)))

"""From the above 3 model, best model is random forest model.. So now we will hyperparameter tuning it.

<h2> <b> Hyperparameter Tuning </b> </h2>
"""

#n_estimators = The number of trees in the forest.
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
n_estimators

"""K-fold method will help us to choose best train and test data so that to get better accuracy result.
We use randomsearchCV for other parameters(like in svm we can pass kernel, C, etc) which we can pass during random forest also. for choosing best value of that parameter , we use randomsearchCV 
"""

from sklearn.model_selection import RandomizedSearchCV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]

# Number of features to consider at every split
max_features = ['auto', 'sqrt']

# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]

# max_depth.append(None)

# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10, 15, 100]

# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 5, 10]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}

print(random_grid)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()

# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 100, cv = 5, verbose=2, random_state=42, n_jobs = 1)

#fit the random forest model
rf_random.fit(X_train,Y_train)

#displaying the best parameters
rf_random.best_params_

rf_random.best_score_

#predicting against test data
y_pred=rf_random.predict(X_test)
#print the erros
print('MAE:', metrics.mean_absolute_error(Y_test, y_pred))
print('MSE:', metrics.mean_squared_error(Y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))
R2 = metrics.r2_score(Y_test,y_pred)
print('R2:',R2)

"""<h2> <b> Save the Model </b> </h2>"""

import pickle
# open a file, where you ant to store the data
file = open('car_price_model.pkl', 'wb')

# dump information to that file
pickle.dump(rf_random, file)

