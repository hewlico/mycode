#!/usr/bin/env python3

round = 0
while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of __________"')
    answer = input()
    if(answer.lower() == "brian" or answer.upper() == "BRIAN"):
        print("Correct")
        break
    elif(round==3):
        print("sorry answer was Brian")
        break 
    else:
        print("Sorry try again")

