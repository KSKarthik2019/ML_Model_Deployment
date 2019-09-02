import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("lsmodel.pkl",'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():    #predict Life Satisfaction
    data = request.get_json(silent=True)
    print(data['GDP_Per_Capita'])
    output = model.predict([np.array(list(data.values()))])
    print(output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)