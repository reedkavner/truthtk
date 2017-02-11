import appengine_config
import logging
from flask import Flask
import donation

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/test')
def test():
    return donation.donate()


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
