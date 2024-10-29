from googlesearch import search
import whois
import time
import random
from colorama import Fore, Back, Style, init

# Initialize colorama and set auto-reset to True
init(autoreset=True)


domains = []
uniq_domains_list = []

available = []
unavailable = []


def get_domains():
    with open('suggested_domains.txt', 'r+') as f:
        for domain_name in f.read().splitlines():

            # Convert to lowercase
            domain_name = domain_name.lower()

            # Collapse multiple words into one string
            domain_name = domain_name.replace(" ", "")

            # Accommodate plain words in the list by searching for the .com and .io version of each plain word
            # Check if the domain_name already ends with .com or .io
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

def check_domains():
    uniq_domains_list.sort(reverse=True)

    counter = 0

    domain_details = None

    for domain_name in uniq_domains_list:
        if domain_name is not None and domain_name != '':
            print(f"{Fore.GREEN}[+] Checking {domain_name}{Style.RESET_ALL}")

            try:
                domain_details = whois.whois(domain_name)
            except whois.parser.PywhoisError as e:
                # print("Exception: {}".format(e))
                # pass
                domain_details = None

            counter = counter + 1

            if domain_details is not None:
                unavailable.append(domain_name)
            else:
                available.append(domain_name)

            if counter >= 40:
                # The whois servers will return "Exception: connect: Connection refused" if you lookup too many
                # domain names using the same whois socket.
                print(f"{Fore.YELLOW}[!] Stopping at 40 lookups. "
                      f"Break your list into smaller pieces and rerun.{Style.RESET_ALL}")
                break

        # Generate a random number of seconds for the upcoming sleep() call.
        sleep_time = random.randint(1, 10)

        sleep_time_string = str(sleep_time)

        print(f"{Fore.GREEN}[+] Sleeping for {sleep_time_string} seconds{Style.RESET_ALL}")

        time.sleep(sleep_time)


def print_availability():
    # print("-----------------------------")
    # print("Unavailable Domains: ")
    # print("-----------------------------")
    #for un in unavailable:
        #print(un)
    print("\n")
    print(f"-----------------------------")
    print(f"{Fore.GREEN}{Style.BRIGHT}Available Domains{Style.RESET_ALL}: ")
    print(f"-----------------------------")
    for available_domain_name in available:
        print(f"{Fore.GREEN}{available_domain_name}{Style.RESET_ALL}")

if __name__ == "__main__":
    get_domains()
    check_domains()
    print_availability()


