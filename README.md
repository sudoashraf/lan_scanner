# A Robust LAN Scanner written in python
This command-line python program is my attempt to make a more robust local area network [LAN] scanner than the usual ones that scan a subnet once using `srp()` method of scapy module in python. Basically the idea is to use the `retry` argument in `srp()` method and pass it through a `for loop` while enumerating the returned list and removing the duplicate entries of the alive hosts.
***
## PRE-REQUISITES
A few pre-requisites for this program to run successfully are :
1. This program requires sudo privilages.
2. The machine on which this program is running must be a part of the subnet to scan.
3. It should have python 3.x insatlled (Python can be installed from its official site - www.python.org). 
4. It should have scapy 2.x installed. Scapy's installation can be carried out / verified with the command: `pip3 install scapy`.

***
## FEATURES
This program has following features:
1. Take user input for the subnet to scan
2. Verify the input for any typo using regex
3. Scan the local subnet rigorously making sure not to miss any host
4. Display a status bar while scanning is in progress
5. Sort the list of hosts scanned based on their IP addresses
6. Display the result is a legible format displaying IPs & MACs for each alive host

***
## A Demo showing the scan

![lan_scanner.gif](lan_scanner.gif)

You can view the code [here](lan_scanner.py) and can leave a :star: if you like it. :smile:
