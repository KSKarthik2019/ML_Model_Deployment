import requests

url = "http://6beabc8c.ngrok.io/predict"
# url= "http://localhost:5000/predict"
predResult = requests.post(url, json={'GDP_Per_Capita':55805.2})
print(predResult.json())