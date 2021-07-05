# Price_prediction_random_forest

In this Machine Learning Project, we are predicting selling price of car based on certain features. Since we need to find the real value, with real calculation, therefore this 
problem is regression problem. We will be using regression machine learning algorithms to solve this problem. We are comparing some of the regression model and choose the best 
out of it based on accuracy and error and then select best parameter for that model using hyperparameter tuning and design the final machine learning model.

I used <strong> Flask </strong> web framework in this project and deployed on <strong>Heroku</strong> on <a href="https://car-price-prdcn.herokuapp.com/"> Click here </a>. 
<h2> About Model </h2><br>
<h3>Steps:</h3>
<ol>
<li> Data Gathering : 
<br><strong> --- Link : </strong> <a href="https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho">https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho</a>
</li><br>
<li> Data preparation
<br> ---  Get the basic idea about the dataset like statistical summary and remove null value if there exist any .
</li><br>
<li>
Feature Engineering
<br> --- Replace the column which does not have any significance and Use Label encoder and one-hot encoding to replace the categorical(object datatype) data into numerical datatype.
</li><br>
<li>
Data Visualization:
<br> --- Use pairplot and heatmap to see the correlation between features .
</li><br>
<li>
EDA (Not done in this project) :
<br> --- EDA is basically used to remove outliers . We are not doing Exploratory data Analysis here, focussing on creating machine learning model. We can see EDA from here : <a href ="https://www.analyticsvidhya.com/blog/2020/08/exploratory-data-analysiseda-from-scratch-in-python/"> Learn EDA from here </a>         
</li><br>
<li>
Feature and Target Variable:
<br> --- Spliiting Features into 2 parts . one of that is target variable and all other columns in other part.
</li><br>
<li>
Feature Importance:
<br> --- Comparing the importance of features using ExtraTreesRegressor
</li><br>
<li>
Splitting dataset into training and testing
</li><br>
<li>
Fitting and Evaluating Different Model
<ul>
<li>
Linear Regression
</li>
<li>
Decision Tree Model
</li>
<li>
Random Forest Model
</li>
</ul><br>
</li>
<li>
Hyperparameter Tuning : 
<br> --- Used for selecting best parameter and I used randomizedSearchCV with 5 fold cross validation for picking best paramater.
</li><br>
<li>
Save the Model
</li><br>

