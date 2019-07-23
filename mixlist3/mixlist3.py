#!/usr/bin/env python3
list1 = ['cisco_nxos','arista_eos','cisco_ios']
#print(list1[1])
print(list1)

#add element to list1
list1.extend(['juniper'])
print(list1)

#add list within another list
list1.append(['10.1.0.1','10.2.0.1','10.3.0.1'])
print(list1)
print(list1[4])
print(list1[4][0])

#create animal list, and print out
animallist = ['cat','dog','mouse']
animallist.append('horse')
animallist.insert(1,'moose')
print(animallist)
