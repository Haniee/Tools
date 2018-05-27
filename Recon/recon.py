#!/usr/bin/python3

import os, sys, re #for opening files and getting arguments
import requests
import threading 

url_list = {}
host = sys.argv[1]
brute_list = []
word_list = []

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
        url_status(domain)
        print(domain)

    print(" ***** Finished searching for easy level subdomains *****")
    try: 
        f = open('wordlist.txt')
    except: 
        print("ERROR: cannot open file")

    for line in f.readlines():
        for d in brute_list:
            domain = line.rstrip() + "-" + d.rstrip()
            url_status(domain)
            print(domain) 
    print(" ***** Finished searching for easy level subdomains *****")


'''def permutation_words():
    def second_level():
    try: 
        f = open('wordlist.txt')
    except: 
        print("ERROR; cannot open file")


#create permutations of words 
def second_level():
    try: 
        f = open('wordlist.txt')
    except: 
        print("ERROR; cannot open file")
    for line in f.readlines():
        for d in brute_list:
            domain = line.rstrip() + "." + d.strip()
'''

def url_status(domain):
    url = "https://" + domain + "/"
    try:
        r = requests.head(url)
        if(r.status_code != 404):
            url_list[url] = r.status_code
            update_list(domain)
            update_wordlist(domain)
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
 	 
def update_wordlist(domain):
    #strip word out of domain 
    word = domain.rstrip(".ns.agency")
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
