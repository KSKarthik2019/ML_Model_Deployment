import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Read Dataset from Local directory
df = pd.read_csv("C:/KSKarthik/Python_Practise/ML_Deployment/LifeSatisfaction.csv")

# Basic info about Dataset
print(df.head())
print(df.info())
print(df.shape)

# No Imputation required since there is no empty value
# We do not need Country column. Hence, you can remove it. Instead, I set it as Index.
df.set_index("Country",inplace=True)
print(df.head())

# Split DataSet into X training set and y target vector.
# this excercise is concentrating on how to deploy a model using Flask framework
X = df["GDP_Per_Capita"].to_frame()
y = df.iloc[:,-1]

# Instantiate LinearRegression Model
lrmodel = LinearRegression()

# Fit the model to the Training Data.  In real case, you can split the dataset with train_test_split()
lrmodel.fit(X,y)

# Pickle the model after training.
pickle.dump(lrmodel,open("lsmodel.pkl","wb"))

# Load the model from the pickle file for testing purpose.
model = pickle.load(open("lsmodel.pkl","rb"))
print(model.predict([[13340.91]]))
