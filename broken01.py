#!/usr/bin/env python 
calc1 = 0.0
calc2 = 0.0
operation = '' 
while(calc1 != "q"):
    print("\n What is the first operator? Or enter  q to quit: ")
    calc1 = input("Enter number: ")
    if calc1.lower() == 'q' or calc1.upper()=='Q':
        print("Exiting")
        break
    try:
        calc1 = float(calc1)
    except:
        print("Invalid input, restarting")
    print("\n What is the second operator? Or enter q to quit: ")
    calc2 = input("Enter Number: ")
    if calc2.lower() == 'q' or calc2.upper() =='Q':
        print("Exiting")
        break
    try:
        calc2 = float(calc2)
    except:
        print("Invalid input, restarting")
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input("Enter operator: ")
    if operation == '+':
        print("\n" + str(calc1) + " + "  + str(calc2) + "=" + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + "=" + str(calc1 - calc2))
    else:
        print("\n Not a valid entry, Restarting....")


