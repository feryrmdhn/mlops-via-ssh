from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from joblib import load

app = FastAPI()

@app.get('/')
def hello_world():
    return {"response": "hello world"}


class IrisSingleRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width:float

mapping_res = {0:'setosa', 1:'versicolor', 2:'virginica'} 

def post_process(pred):
    return  mapping_res[pred]

@app.post('/iris')
def iris(request:IrisSingleRequest):
    formatted_features = [[request.sepal_length,request.sepal_width,request.petal_length,request.petal_width]]
    
    # load model
    model = load('model.sav')
    result = model.predict(formatted_features)

    return {"result response": post_process(result.tolist()[0])}