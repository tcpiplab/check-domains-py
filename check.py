#!/usr/bin/python3
from googlesearch import search
import whois

domains = []
uniq_domains_list = []

available = []
unavailable = []


def getDomains():
    with open('domains.txt', 'r+') as f:
        for domain_name in f.read().splitlines():

            # Convert to lowercase
            domain_name = domain_name.lower()

            # Collapse multiple words into one string
            domain_name = domain_name.replace(" ", "")

            # Accommodate plain words in the list
            if (domain_name.endswith(".io") is False) and (domain_name.endswith(".com") is False):
                domain_name = domain_name + ".com"

            # Add the .com domain_name to the list
            domains.append(domain_name)

            # Also check for .io availability
            if domain_name.endswith(".com"):
                domain_name_io = domain_name.replace(".com", ".io")
                domains.append(domain_name_io)

            # Remove duplicates
            for i in domains:
                if i not in uniq_domains_list:
                    uniq_domains_list.append(i)

def run():
    uniq_domains_list.sort()

    for dom in uniq_domains_list:
        if dom is not None and dom != '':
            #print("Checking {}".format(dom))
            details = whois.query(dom, slow_down=1)
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


