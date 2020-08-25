
# A Python program to scan a local area network [LAN]

# Importing scapy.all to generate and send/recv packets using scapy module
from scapy.all import ARP,Ether,srp
# Importing itemgetter to sort the client list
from operator import itemgetter
# Importing regular expression to verify the input
import re

# Defining the scanning function
def scan(ip):

    # Putting eveything in a try block especially to catch KeyboardInterrupt
    try:

        # Generating the ARP header with the destination as the network to scan
        arp_request = ARP(pdst=ip)

        # Generating the Ethernet header specifying the destination MAC as broadcast
        ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")

        # Combining the headers to form a broadcast packet
        broadcast = ether_frame/arp_request

        # Declaring an empty client list to collective responses on each iteration (this list will have duplicate entries)
        clients = []

        # Print a status message
        print("\nScanning in Progress ...")

        # Declaring a variable that will show progress
        bar = 0

        # Print initial progress bar with 0% progress
        print('\n\r[{0}{1}]'.format('#'*bar, '-'*(30-bar)) + ' ' + str(int(bar/30*100)) + '% ', end="")

        # for loop for callinf srp() three times for robustness
        for packet in range(0,3):

            # Using srp() methong to send and receive ARP packets
            # Using timeout=2 & retry=3 argument to try not to miss hosts
            # And collecting the responses in answered variable
            answered = srp(broadcast, timeout=2, retry=3, verbose=False)[0]

            # Appending the responses in the above declared list (this will have duplicate entries)
            clients.append(answered)

            # Incrementing the progress variable to show the progress after each iteration
            bar += 10

            # Printing the progress bar after each iteration
            print('\r[{0}{1}]'.format('#'*bar, '-'*(30-bar)) + ' ' + str(int(bar/30*100)) + '% ', end="")

        # Print another status message after scan is completed
        print("\n\nFinished Scanning.\n")

        # Declaring another empty list to store ip & mac for eah hosts (this list will also have duplicate entries)
        client_list = []

        # A for loop to iterate through the sendrcvlist and refer each tuple
        for client in clients:

            # Another for loop to iterate through each tuple of the list
            for item in client:

                # Creating a dictionary to store ip & mac of each alive host
                client_dict={"ip": item[1].psrc, "mac": item[1].hwsrc}

                # Appending to the above created list to make a list of dictionaries for clients
                client_list.append(client_dict)

        # Create another list to remove the duplicate entries from the above scan
        hosts = [i for n, i in enumerate(client_list) if i not in client_list[n + 1:]]

        # Finally return the processsed list containing ip & mac for each alive host
        return hosts

    # Handling user interrupt by printing the following & returning empty list
    except KeyboardInterrupt:
        print("\n\nScanning aborted by user.\n")
        return []

# Putting eveything in a try block especially to catch KeyboardInterrupt
try:

    # This is the first statement to get executed asking for input
    subnet = input("\nEnter a local subnet to scan [For eg. 10.0.0.0/24]: ")

    # Validating the user input for any typo
    if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}", subnet) == None:
        print("\nIncorrect subnet. Please check.\n")

    else:

        # Calling the scan function by passing the requested subnet & collecting list in clients
        clients = scan(subnet)

        # Checking if the scan result is not an empty list
        if clients:

            # Print status for Generating List
            print("Generating List.\n")

            # A wait for 2 secs because without it the output is too quick
            time.sleep(2)

            # Sorting the list based on host IPs
            clients.sort(key=itemgetter("ip"))

            # Printing the result in a legible format
            print("   IPs\t\t\t    MACs\n------------------------------------------")

            # for loop to access each (host)item in the (clients)list
            for host in clients:

                # Access each host's ip & mac by specifying keys ["ip"] & ["mac"]
            	print(" " + host["ip"] + "\t\t" + host["mac"])

            print("------------------------------------------\n")

        # if scan resulted in an empty list
        else:
            print("Scan result was empty.\n")

# Handling user interrupt by printing the following
except KeyboardInterrupt:
    print("\n\nAborted by user. Exiting program.\n")
