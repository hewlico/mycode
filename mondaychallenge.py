#!/usr/bin/env python3
pets = [2,"cats",3,"dogs"]
#print("I have", str(pets[0]),str(pets[1]) , " and ", str(pets[2]),str(pets[3]+"."))
print("I have {2} {1} and {0} {3}.".format(*pets))
