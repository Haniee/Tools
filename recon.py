#!/usr/bin/python3

import os, sys, re #for opening files and getting arguments
import requests
import threading 

url_list = {}
host = sys.argv[1]
brute_list = []

#bruteforce list 

def bruteforce():
	#open the wordlist file 
    print("")
    print(" ***** Testing for subdomains using bruteforce *****")
    try: 
        f = open('wordlist.txt')
    except: 
        print("ERROR: cannot open file")
    for line in f.readlines():
        domain = line.rstrip() + "." + host
        url_status(domain, line)
        print(domain)
       


def second_level():
    print("potato")


def url_status(domain, word):
    url = "https://" + domain + "/"
    try:
        r = requests.head(url)
        if(r.status_code == 200 or r.status_code == 401 or r.status_code == 403):
            url_list[url] = r.status_code
            update_list(domain)
            update_wordlist(word)
    except: 
        print("")
    
def check_word(word):
    try:
        f = open('wordlist.txt','r')
    except: 
        print("ERROR: failed to open file")
    for line in f.readlines():
        if(line == word):
            return False
    return True 

def check_list(domain):
    for d in brute_list: 
        if(d == domain):
            return False 
    return True 

def update_list(domain):
    brute_list.append(domain)
 	 
def update_wordlist(word):
    #check if word is already in list 
    if(check_word(word) == True):
        try: 
            with open('wordlist.txt','a') as f:
                f.write(word)
        except: 
            print("ERROR: cannot open file")



if __name__ == "__main__":
    try:
        bruteforce()
    except:
        print("ERROR: Failed to complete bruteforce")
    print("")
    print("***** Possible Subdomains List for " + host + " *****")
    print("")
    for u in url_list.items():
        print(u)
    print("")
