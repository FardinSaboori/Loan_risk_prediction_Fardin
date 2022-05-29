import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('models/model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('home.html')
    # return "<h1>hello</h1>"


@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)

    output = round(prediction[0], 2)
    if output == 1:
        output = 'Fully paid'
    else:
        output = 'Charged off'
    return render_template('home.html', prediction_text='This Loan will be {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)