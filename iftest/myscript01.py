#!/usr/bin/env python3

print("This program rates network speeds that are entered by the user")
print("Please enter values in increments of 10 from 10 - 100Mbps")

try:
    networkspeed = input("Enter network speed in Mbps: ")
    print("You have entered " + str(networkspeed) + " Mbps")
    if networkspeed: 
        print("User has entered nework speed, please wait till we rate it")
    if networkspeed < 10:
        print("Network score of Poor")
    elif networkspeed < 50:
        print("Network speed is Good")
    elif networkspeed >= 50:
        print ("Network speed is Excellent") 
    else:
        print("User entered: " + str(networkspeed) + " this is an incorrect value." )
except:
    print("User entered invalid data")
print("Exiting Script")
