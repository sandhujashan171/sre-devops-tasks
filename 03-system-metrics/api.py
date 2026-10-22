from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Gauge, generate_latest
import psutil

app = FastAPI()

# Define the exact metric names Prometheus will look for
cpu_gauge = Gauge('cpu_usage_percent', 'Current CPU utilization')
mem_gauge = Gauge('memory_usage_percent', 'Current memory utilization')

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    # Capture the live hardware data
    cpu_gauge.set(psutil.cpu_percent())
    mem_gauge.set(psutil.virtual_memory().percent)
    
    # Output in the specific plaintext format Prometheus requires
    return generate_latest()
