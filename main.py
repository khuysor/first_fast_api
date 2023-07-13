from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'huysor'}}

@app.get('/about')
def about():
    return {'data':{' page':'aboutpage'}}
