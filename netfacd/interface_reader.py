#!/usr/bin/env python3 
import netifaces

def getadd():
    #print(netifaces.interfaces())

    userinput = input("Enter adapter to get IP and Mac address: ")
    for i in netifaces.interfaces():
        #print('\n ***** Details of Interface - ' + i + ' *******')
        if(i in  userinput):
            #print('\n ***** Details of Interface - ' + i + ' *******')
            try:
                print("MAC add of intf: " + str(i) + " ", netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #Prints intf mac
                print("IP add of intf: " + str(i) + " " , netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #Prints intf IP
            except:
                print('Could not collect adapter info')
    

def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print('\n ***** Details of Interface - ' + i + ' *******')
        try:
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #Prints intf mac
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #Prints intf IP
        except:
            print('Could not collect adapter info')



getadd()


