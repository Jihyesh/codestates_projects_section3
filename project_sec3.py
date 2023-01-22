from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.linear_model import RidgeCV, LassoCV

model = pickle.load(open('model/model.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    # data1 = request.form['a']
    # data2 = request.form['b']
    # data3 = request.form['c']
    # data4 = request.form['d']
    # data5 = request.form['e']
    # data6 = request.form['f']
    # data7 = request.form['g']
    # data8 = request.form['h']
    # data9 = request.form['i']
    # data10 = request.form['j']
    # data11 = request.form['k']
    # arr = np.array([[data1,data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]])
    float_features = [float(x) for x in request.form.values()]
    arr = [np.array(float_features)]
    pred = model.predict(arr)

    return render_template('index.html', price= pred)


# @app.route("/", methods=['GET','POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#     if request.method == 'POST':
#         avg_temp = float(request.form['avg_temp'])
#         min_temp = float(request.form['min_temp'])
#         max_temp = float(request.form['max_temp'])
#         rain_fall = float(request.form['rain_fall'])
    
#     price = 0

#     data = ((avg_temp,min_temp,max_temp,rain_fall),)
#     arr = np.array(data, dtype=np.float32)

#     x_data = arr[0:4]
#     dict = sess.run(hypothesis, freed_dict={X:x_data})

#     price = dict[0]
#     return render_template('index.html',price=price)

if __name__ =='__main__':
    app.run(debug=True)