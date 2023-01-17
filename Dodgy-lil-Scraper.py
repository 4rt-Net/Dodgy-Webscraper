#!/bin/python

'''
Simple Webscraper using proxies and random user-agents - for educational purposes only!

Do not use this code on websites that you are not authorized to scrape. 
'''

import random
from random import randrange
import requests
from collections import namedtuple

#Reads urls from text file (addresses.txt)
def read_addresses():
    with open("addresses.txt", "r") as file:
        addresses = file.read().splitlines()
    return addresses

#list of Proxy servers to use for each request - Add proxy servers
http_proxies = ["10.0.0.1:8888", "", "", "", ""]

#list of User-agents to use for each request - Add user-agent strings
user_agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
"",
"",
"",
"",
"",
]

#choose random user-agent from list
def random_agent():
    agent_index = randrange(0, len(user_agents))
    headers = {"user-agent": "{}".format(user_agents[agent_index])}
    return headers

#choose random proxy from list
def random_proxy():
    proxy_index = randrange(0, len(http_proxies))
    proxy = {"http://": "{}".format(http_proxies[proxy_index])}
    return proxy

#Requests site data
def scraper_request(ip_address):
    r = requests.get(address, proxies=random_proxy(), headers=random_agent())
    return r.text, r.cookies

##All results are saved in sites.html file with "New Site:" break between sites. 
if __name__ == "__main__":
    addresses = read_addresses()
    for address in addresses:
        scrape_results = scraper_request(address)
        Scraper = namedtuple("Scraper", ["html", "cookies"])
        scrape = Scraper(scrape_results[0], scrape_results[1])
        #Uncomment to print retrieved data to terminal
        #print(scrape.html)
        #print(scrape.cookies)
        with open(f"sites.html", "a", encoding="utf-8") as my_file:
            my_file.write(str(scrape.html))
            my_file.write(str(scrape.cookies)+"\n\n\n\n\n"+("#"*150)+"\n\n[+] New Site:\n\n\n\n\n")
