from google.appengine.ext import ndb

#venue, title, perfid, cast, date_time
class Tweet(ndb.Model):
	text = ndb.StringProperty()
	tid = ndb.IntegerProperty()
	donation = ndb.IntegerProperty()
	donation_successful = ndb.BooleanProperty()
	date_added = ndb.DateTimeProperty(auto_now_add=True)