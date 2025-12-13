import json
from logging import Logger

from fastapi import FastAPI


logger = Logger("SmartToy")

app = FastAPI(title="SmartToy")

@app.get("/")
def get_home():
    logger.info(f"The app: {str(app)}")
    return {
        "message": f"Hello, I am SmartToy!"
    }