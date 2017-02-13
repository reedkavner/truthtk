import appengine_config
import logging
from flask import Flask, render_template
import tweets
import urllib2
import propublica
import models

app = Flask(__name__)

@app.route('/')
def home():
	total = 0
	q = models.Tweet.query().fetch(limit=1000)
	for t in q:
		total += t.donation

	return render_template('index.html', total=total)

@app.route('/admin/check')
def test():
	return str(tweets.check())


@app.errorhandler(500)
def server_error(e):
	# Log the error and stacktrace.
	logging.exception('An error occurred during a request.')
	return 'An internal error occurred.', 500
