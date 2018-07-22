
from logging.handlers import RotatingFileHandler
from flask import Flask, request

import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('github.log', maxBytes=10000, backupCount=1)
logger.addHandler(handler)

@app.route('/', methods=['GET', 'POST'])
def endpoint():
    logger.info(request.get_data().decode('utf8'))
    return "Success"

if __name__ == '__main__':
    app.run()
