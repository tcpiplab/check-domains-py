#!/usr/bin/python3
import whois

domains = []


available = []
unavailable = []


def getDomains():
    with open('domains.txt', 'r+') as f:
        for domainName in f.read().splitlines():
            domains.append(domainName)

def run():   
    for dom in domains:
        if dom is not None and dom != '':
            details = whois.query(dom)
            if details is not None:
                unavailable.append(dom)
            else:
                available.append(dom)

def printAvailability():
    print("-----------------------------")
    print("Unavailable Domains: ")
    print("-----------------------------")
    for un in unavailable:
        print(un)
    print("\n")
    print("-----------------------------")
    print("Available Domains: ")
    print("-----------------------------")
    for av in available:
        print(av)
    

if __name__ == "__main__":
    getDomains()
    run()
    printAvailability()


