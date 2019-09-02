# ML_Model_Deployment
Ojbective: How to deploy a machine learning model using Flask framework

Solution: This excercise shows you how to deploy a machine learning (ML) model using Flask framework. 

1. This project is created with PyCharm IDE.

2. It has below-mentioned files: 
   (a). LifeSatisfactionModel.py
   (b). webservice.py
   (c). request.py
   (d). templates folder, which consists of index.html file. 
   
3. Environment: Python 3.7, NumPy, Pandas, Scikit Learn, Flask and Ngrok. 

4. LifeSatisfactionModel.py ==> It uses a dataset, which comprises of GDP_Per_Capita and Life Satisfaction Value. 
Since it is more into how we can deploy, It does not do any EDA, cross validation. 
It creates a regression model using Scikit Learn LinearRegression() 

5. webservice.py ==> It is a simple Flask app, which acts as a webservice.

6. templates folder ==> it contains index.html file, which we use for checking the webservice. 

7. request.py ==> It calls the webservice and predict the result, based on the value it passes to webservice. 
