#!/usr/bin/env python3

def sortlist(listexm):
    shortwords = 0
    mediumwords = 0
    longwords = 0

    for item in listexm:
        if(len(item) <  5):
            shortwords += 1
        elif(len(item) <= 10 ):
            mediumwords += 1
        else:
            longwords +=1
    print ("Short words " + str(shortwords))
    print ("Medium words " + str(mediumwords))
    print ("long words " + str(longwords))



def main():
    examplelist = ['banna','blueberries','nut','accorns']
    sortlist(examplelist)

main()
