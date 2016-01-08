import telepot
import time
from pprint import pprint

class MyBot(telepot.Bot):
	def handle(self,msg):
	        receivedText  = msg[u'text']
	        messageSender = msg[u'from'][u'id']

        	self.sendMessage(messageSender, receivedText)

def main():
	bot = MyBot('176703220:AAGLqtZ531Lbmjguzv-9W4ui9CL3sKXgYK8')
	bot.notifyOnMessage()

	while 1:
		time.sleep(10)
