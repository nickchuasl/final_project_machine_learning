from flask import Flask, render_template, request
import numpy as np
from pickle import load

loaded_model = load(open('model.pkl', 'rb')) 
loaded_X_scaler = load(open('X_scaler.pkl', 'rb'))
loaded_y_scaler = load(open('y_scaler.pkl', 'rb')) 



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods = ['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    arr = np.asarray([int_features])
    arr = loaded_X_scaler.transform(arr)
    reshape_arr = arr.reshape(1, -1)
    prediction_data = loaded_model.predict(reshape_arr)
    prediction_data = round(prediction_data[0][0],0)
    return render_template('index.html', prediction_text = f'House Price prediction is: {prediction_data}')

# if __name__ == "__main__":
#     app.run(debug=True)

app.run('127.0.0.1', 5000)