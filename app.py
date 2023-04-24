# Importing all the modules
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd


# Defining flask app
app = Flask(__name__)

# Loading the pickle files. scaling.pkl is for the transformation and regression.pkl is for the prediction
scalar = pickle.load(open('scaling.pkl', 'rb')) 
reg_model = pickle.load(open("regression.pkl", "rb"))

# Creating the first root into the Home page. That is, once we run this file, we will be navigated into the 'home.html' page
@app.route('/')
def home():
    # Rendering an HTML page called 'home.html'
    return render_template('home.html')


# Creating a POST API were we can reach the prediction model with any tools like Postman.
# The data will be in below format
# {
#     'data':{
#         'CRIM': 0.98,
#         'ZN' : 87
#         ...
#         ...
#     }
# }
@app.route('/predict_api', methods = ['POST'])
def predict_api():

    # Reading the data from the call
    data = request.json['data']
    print(data)

    # Shaping the data from json to list:  [[{'CRIM': 0.98, 'ZN': 87}]]
    transform  = np.array(list(data.values())).reshape(1,-1)

    # Applying transformations to the dataset. Scaling in this case
    new_data = scalar.transform(transform)

    # Prediction 
    output = reg_model.predict(new_data)

    # Printing the output. It will be in two dimension. So we need to use [0]
    print(output[0])

    return jsonify(output[0])


# Running the app
if __name__ == "__main__":
    app.run(debug=True)