#  build an interface for the model testing
# import the necessary libraries
from flask  import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle
# load the model
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

# create a Flask app
app = Flask(__name__)

# define the home route
@app.route('/')
def home():
    return render_template('index.html')

# define the predict route
@app.route('/predict', methods=['POST'])    
def predict():
    # get the input text from the form
    input_text = request.form['text']
    
    # make a prediction using the model
    prediction = model.predict([input_text])[0]
    
    # return the prediction as a JSON response
    return jsonify({'prediction': prediction})

# run the app
if __name__ == "__main__":
    app.run(debug=True)