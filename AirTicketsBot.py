import telepot
import time
import urllib2
import urllib
from pprint import pprint
from skyscanner import flights

class MyBot(telepot.Bot):
	def handle(self,msg):
	        receivedText  = msg[u'text'] 
	        messageSender = msg[u'from'][u'id']

        	self.sendMessage(messageSender, receivedText)

	def listenNotification(self):
		self.notifyOnMessage()

		while 1:
			time.sleep(10)

# Trying to connect to a site
urlSite = 'https://www.google.com.br/?gws_rd=ssl'
def getResponse():
	response = urllib2.urlopen(urlSite)
	html = response.read()
	print html

def sendPost(dataSent):
	dataSent = {'lst-ib':'sabaton'}
	encData = urllib.urlencode(dataSent)
	req = urllib2.Request(urlSite,encData)
	response = urllib2.urlopen(req)
	the_page = response.read
