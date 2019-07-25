user = input("Would you ike to quiye?")
while user.lower != 'q'
    try:
        a = int(input("Please enter interger"))
    except ValueError:
        print("not an integer")
        continue

    print(a+20)
    user = input("Would you like to quit?")
    if user.lower()== 'q':
        break   
