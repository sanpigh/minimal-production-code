from fastapi import FastAPI

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
