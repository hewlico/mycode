#!/usr/bin/env python3
#Creating list and use a print
my_list = ["192.168.0.5",5060,"UP"]
print("This first item in the list (IP): " + my_list[0])
print("The second item in the list (port): "+ str(my_list[1]))
print("The last item in the list (state): "+my_list[2])
new_list = [5060,80,55,"10.0.0.1","10.20.30.1","ssh"]

#complete print
print("When I ssh into IP: " + str(new_list[3]) +" or " + str( new_list[4]) + " .I am unable to ping ports " + str(new_list[:-3]))
