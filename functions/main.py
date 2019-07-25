#!/usr/bin/env python3
""" This takes and prints out IPs"""

def commandpush(filename): 
    #prints stuff
    file = open(filename)
    lines = file.readlines()
    for item in lines:
        print('\n Handshaking ... connecting with ' + item)
    file.close()

def devicereboot(ip_address):
    #prints stuff
    print('\n List of IPs')
    for ip_a in ip_address:
        print(' IP address is: ' + ip_a) 

def main():
    #work2do
    filename = 'ip.txt'
    ipaddresses = ["10.1.0.1", "10.1.1.245", "10.1.2.4"]
    print("\n Welcome to the network device command pusher")
    print("\n Data set found \n")
    commandpush(filename)
    devicereboot(ipaddresses)

main()
