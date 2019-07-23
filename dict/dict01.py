#!/usr/bin/env python3

#creates switch dictionary 
switch = {'hostname':'sw1','ip':'10.0.1.1','version':'1.2','vendor':'cisco'}
print(switch['hostname'])
print(switch['ip'])

# request non existent key
#print(switch['lynx'])

#request non existent key via get method 
print("Second test - .get()")
print(switch.get('version'))

print("third test - .get()")
print(switch.get('version'))

print("Fourth test - keys()")
print(switch.keys())

print("Fith test - .values()")
print(switch.keys())


#modifying dict
print("Sixth test - .pop()")
switch.pop('version') #rm key and value pair 
print(switch.keys())
print(switch.values())

print("Seventh test - ADD a new value")
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())

print("Eight Test - ADD a new value")
switch['password'] = '12345'
print(switch.keys())
print(switch.values())

