#!/usr/bin/env python3
vendors = ["cisco","juniper","big ip","f5","arista"]
approved_vendors = ["cisco","juniper","big ip"]
for vendor in vendors:
    print("The venor is: " + vendor)
    if vendor not in approved_vendors:
        print(" - Not an approved vendor")
print("\n Our loop hs ended") 
