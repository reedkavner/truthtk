import appengine_config
from secrets import twitter_auth as ta
import twitter
import models
import logging
import propublica

def is_in_db(tid):
	q = models.Tweet.query(models.Tweet.tid == tid)
	return False if q.count() == 0 else True

def calculate_donation(text):
	total = 1
	
	if 'FAKE NEWS' in text:
		total += 1

	mentions = ['@nytimes', '@cnn']	
	if any(i in text.lower() for i in mentions):
		total += 1

	if 'failing @nytimes' in text.lower():
		total += 1

	if '@propublica' in text.lower():
		total += 5

	return total

def check():
	api = twitter.Api(consumer_key=ta['consumer_key'],
	                  consumer_secret=ta['consumer_secret'],
	                  access_token_key=ta['access_token'],
	                  access_token_secret=ta['access_token_secret'])

	statuses = api.GetUserTimeline(screen_name='realdonaldtrump', trim_user=True, count=5)

	total = 0
	for s in statuses:
		logging.debug("Reading tweet {}: {}".format(s.id, s.text))
		if 'fake news' in s.text.lower():
			if is_in_db(s.id) == False:
				donation = calculate_donation(s.text)
				total = total + donation
				try:
					donation_success = propublica.donate(donation, s.id)
				except:
					logging.warning("Something went wrong with donation for tid {}".format(s.id))
					donation_success = False
				record = models.Tweet(
					text = s.text,
					tid = s.id,
					donation = donation,
					donation_successful = donation_success)
				record.put()
			 
			else:
				break
	
	return total