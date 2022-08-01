#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#'step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest','newbalanceDest', 'bal_diff_orig', 'typeId',
#'day', 'weekday','sin_hour', 'cos_hour'

import numpy as np
import math
import pickle
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
#model = pickle.load(open("model.pkl", 'rb'))
with open('fraudpredmodel.pkl','rb') as f:
        model=joblib.load(f)

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'typeid': "Type"}, {'typeid': "CASH_IN"}, {'typeid': "CASH_OUT"}, {'typeid': "DEBIT"},
               {'typeid': 'PAYMENT'}, {'typeid': "TRANSFER"}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    
    if input_data[0].isdigit() == True & input_data[1].isdigit() == True & input_data[2].isdigit() == True & input_data[3].isdigit() == True & input_data[4].isdigit() == True & input_data[5].isdigit() == True:
        pass
    else:
        print(ValueError)

    if input_data[6] == 'PAYMENT':
        input_data[6] = 0
    elif input_data[6] == 'TRANSFER':
        input_data[6] = 1
    elif input_data[6] == 'CASH_OUT':
        input_data[6] = 2
    elif input_data[6] == 'DEBIT':
        input_data[6] = 3
    elif input_data[6] == 'CASH_IN':
        input_data[6] = 4    
    else:
        print(ValueError)

    input_values = [x for x in input_data]
    y=float(input_values[0])         #step
    w=float(input_values[1])         #amount
    z=float(input_values[2])         #oldbalanceOrg
    a=float(input_values[3])         #newbalanceOrig
    b=float(input_values[4])         #oldbalanceDest
    c=float(input_values[5])         #newbalanceDest
    d=abs(z-a)                       #bal_diff_orig 
    e=float(input_values[6])         #typeid
    f=y//24                          #day
    g=y//168                         #weekday
    h=np.sin((math.pi*y)/(30*24))    #sin_hour
    i=np.cos((math.pi*y)/(30*24))    #cos_hour
    #arr_val = [np.array(input_values)]
    #arr_val = np.array([input_values]).reshape(1,-1)
    
    arr_val=np.array([y,w,z,a,b,c,d,e,f,g,h,i]).reshape(1,-1)
    prediction = model.predict(arr_val)
    
    if prediction == 0:
        output ="Not_Fraud"
    else:
        output ="Fraud"
    
    return render_template('index.html', prediction_text=" The predicted transaction is {}".format(output),
                           data=[{'typeid': "Type"}, {'typeid': "CASH_IN"}, {'typeid': "CASH_OUT"}, {'typeid': "DEBIT"},
                                 {'typeid': 'PAYMENT'}, {'typeid': "TRANSFER"}])


if __name__ == '__main__':
    app.run(debug=True)

