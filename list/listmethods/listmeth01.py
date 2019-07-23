#!/usr/bin/env python3
proto = ["ssh","http","https"]
protoa = ["ssh","http","https"]
print(proto)

proto.append('dns')   #append dns to proto list 
protoa.append('dns')  #append dns to prota list
print(proto)

proto2 = [22,80,443,53]  #common port list
proto.extend(proto2)     #pass proto2 as args
print(proto)

protoa.append(proto2)    #pass proto2 as an arg to the append method
print(protoa)
#proto.extend('dns') #line adds d , n ,s

#insert element to list 
proto.insert(2,"test")
print(proto)
#print(proto[1])

