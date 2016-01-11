import telepot
import time
from pprint import pprint

class MyBot(telepot.Bot):
	def handle(self,msg):
	        receivedText  = msg[u'text'] 
	        messageSender = msg[u'from'][u'id']

        	self.sendMessage(messageSender, receivedText)

	def listenNotification(self):
		self.notifyOnMessage()

		while 1:
			time.sleep(10)
