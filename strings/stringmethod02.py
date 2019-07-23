#!/usr/bin/env python3
""" ALTA3 Research || Author RZFeeser@alta.com"""

def main():
    #create small string
    lilstring = "Alta 3 research offers classes on Python coding"
    newlist = lilstring.split(" ") # this returns a list 
    print(newlist)

    #create a list of strings 
    myiplist = ["192","168","0","12"]

    #set single ip as the result
    singleip = ".".join(myiplist)
    print(singleip)

#main function call
main()
