#!/bin/python

'''
Simple Webscraper using proxies and random user-agents - for educational purposes only!

Do not use this code on websites if you are not authorized to do so. 

Please keep in mind:
Obfuscating your user-agent may be considered a violation of a website's terms of service, 
Additionally, certain uses of user agent spoofing, such as scraping content or automating clicks on ads, 
may be considered illegal in some cases.
'''

import random
from random import randrange
import requests
from collections import namedtuple

#Reads ip address from a text file (ip_addresses.txt)
def read_addresses():
    with open("addresses.txt", "r") as file:
        addresses = file.read().splitlines()
    return addresses

#list of Proxy servers to use for each request (random)
http_proxies = ["IP:Port", "", "", "", ""]

#list of User-agents to use for each request (random)
user_agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
"",
"",
"",
"",
"",
]


def random_agent():
    agent_index = randrange(0, len(user_agents))
    headers = {"user-agent": "{}".format(user_agents[agent_index])}
    return headers

def random_proxy():
    proxy_index = randrange(0, len(http_proxies))
    proxy = {"http://": "{}".format(http_proxies[proxy_index])}
    return proxy

def scraper_request(ip_address):
    r = requests.get(address, proxies=random_proxy(), headers=random_agent())
    return r.text, r.cookies

#end result: Requests data from each address in addresses.txt and writes the received data to a sites.html file. 
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