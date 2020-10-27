#!/usr/bin/python3 

import enchant 

def bruteforce(arr):
	dict1 = enchant.Dict("en_US")
	s = ''.join(chr(x) for x in arr)
	
	if dict1.check(s):
		return s
	return -1
	
	

if __name__ == "__main__":
	e_txt = input("Enter your encrypted text: ")

	pt_arr = []
	foundFlag = False
	n = 1

	while foundFlag is not True:
		for t in e_txt:
			curr = ord(t) - n	
			pt_arr.append(curr)
		pt = bruteforce(arr)
		if pt is not -1:
			foundFlag = True
			print(pt)

