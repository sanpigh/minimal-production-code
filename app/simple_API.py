
import joblib
from fastapi import FastAPI
from requests import models

app = FastAPI()

@app.get('/')
def index():
    return {'ok' : True}

@app.get('/multiply')
def multiply_fuction(a, b):
    return {'a' : a, 'b' : b, 'a*b' : float(a)*float(b)}

@app.get('/add')
def add_fuction(a, b):
    return {'a' : a, 'b' : b, 'a+b' : float(a)+float(b)}

@app.get('/dif')
def dif_fuction(a, b):
    return {'a' : a, 'b' : b, 'a-b' : float(a)-float(b)}


@app.get('/prediction')
def prediction-using-model-joblib_fuction():
    input = pd.DataFrame({
        'key' : 'nothing', 
        'pickup_datetime'  : '2015-01-27 13:08:24 UTC', 
        'pickup_longitude' : -73.973320, 
        'pickup_latitude'  : 40.835,
       'dropoff_longitude' : -73.981430, 
       'dropoff_latitude'  : 40.743835,  
       'passenger_count'   : 1
    })
    model = joblib.load(model.joblib)
    fare = model.predict(input)
    print(fare)
    return True
#    return {'fare' : fare}



