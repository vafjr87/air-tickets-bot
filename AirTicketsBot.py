import telepot
import time
from pprint import pprint

bot = telepot.Bot('176703220:AAGLqtZ531Lbmjguzv-9W4ui9CL3sKXgYK8')

print "Running AirTickets"


def handle_message(msg):
	pprint(msg)

bot.notifyOnMessage(handle_message)

while 1:
	time.sleep(10)
