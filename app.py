from flask import Flask
from src.logger import logging

app= Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("We are testing another method of logging")
    return "Welcome to End-to-End ML Project"

if __name__=="__main__":
    app.run(debug= True)