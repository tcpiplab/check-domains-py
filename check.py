from googlesearch import search
import whois
import time

domains = []
uniq_domains_list = []

available = []
unavailable = []


def get_domains():
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

def check_domains():
    uniq_domains_list.sort(reverse=True)

    counter = 0

    domain_details = None

    for domain_name in uniq_domains_list:
        if domain_name is not None and domain_name != '':
            print("Checking {}".format(domain_name))

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
                print("Stopping at 40 lookups. Break your list into smaller pieces and rerun.")
                break

        time.sleep(7)


def print_availability():
    # print("-----------------------------")
    # print("Unavailable Domains: ")
    # print("-----------------------------")
    #for un in unavailable:
        #print(un)
    print("\n")
    print("-----------------------------")
    print("Available Domains: ")
    print("-----------------------------")
    for av in available:
        print(av)

if __name__ == "__main__":
    get_domains()
    check_domains()
    print_availability()


