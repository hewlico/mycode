#!/usr/bin/env python3 
ipchk = input("Apply an IPv4 address") #prompt user for input 

if ipchk == "192.168.70.1": #if ip matches
    print("IP is " + ipchk + " this is not recommended")
elif ipchk: #set to true if any value is provided 
        print("IP set to: " + ipchk)
else: #no user data entered
    print("User must enter data")

