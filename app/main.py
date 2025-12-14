from logging import Logger

from fastapi import FastAPI


logger = Logger("SmartToy")

app = FastAPI(title="SmartToy")

@app.get("/")
def get_home():
    return {
        "message": "Hello, I am SmartToy!"
    }