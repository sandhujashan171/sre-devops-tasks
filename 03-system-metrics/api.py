from fastapi import FastAPI
from system_util import get_system_metrics

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello from your Ubuntu server!"}

@app.get("/metrics")
def read_metrics():
    return get_system_metrics()
