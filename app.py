import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model2 = pickle.load(open('model2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    k=np.array(int_features)
    print(k[0])
    final_features = [np.array(int_features)]
    print(final_features[0])
    if k[0]>6000 or k[1]>3000 or k[4]>15:
        output='NA'
    else:
        prediction = model2.predict(final_features)

        output = prediction[0]

    return render_template('index1.html', prediction_text='Rating {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)