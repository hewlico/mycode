#!/usr/bin/env python3

#open file
dnsfile = open("dnsservers.txt")

dnslist = dnsfile.readlines()

for dns in dnslist:
    print(dns,end="")
dnsfile.close()
