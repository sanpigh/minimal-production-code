

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
def prediction-using-model-joblib_fuction(input):
    model = load_model()
    fare = model.predict(input)
    return {'fare' : fare}
