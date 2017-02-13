# TruthTK

TruthTK is a bot that donates to ProPublica whenever @realDonaldTrump tweets "fake news". See http://www.truthtk.com/ for more.

### Installation
TruthTK is built to work on Google App Engine. You'll need to do a few things:
- Install the dependencies in requirements.txt
- Edit the 'application' field in app.yaml to match your GAE application's name
- Using secrets_example.py as a template, add your own Twitter keys and billing information. Save the file as secrets.py
- The python-twitter module needs a one-line modification to work on a local environent: https://github.com/reedkavner/python-twitter/commit/6fcc44059aaf56278deaf6f6176bc9339780661f
- appengine_config.py is configured to look for lobraries in env/lib/python2.7/site-packages, the default path for Virtualenv. Change that if you're keeping libraries somewhere else.

### Disclaimer
This software uses your credit card number to make donations on your behalf. It is offered as-is and I make no guarantees that it will work as intended. Please be careful. I reccomend setting up a throwaway credit card number with https://privacy.com just in case things go crazy.
