s = input("Enter the string: ")
state = 0
for i in s:
    if (state == 0):
        if (i == 'a'):
            state = 1
        elif (i == 'b'):
            state = 3
        else:
            print("Invalid symbol")
            break
    elif (state == 1):
        if (i == 'a'):
            state = 0
        elif (i == 'b'):
            state = 2
        else:
            print("Invalid symbol")
            break
    elif (state == 2):
        if (i == 'a'):
            state = 3
        elif (i == 'b'):
            state = 1
        else:
            print("Invalid symbol")
            break
    elif (state == 3):
        if (i == 'a'):
            state = 2
        elif (i == 'b'):
            state = 0
        else:
            print("Invalid symbol")
            break
if (state == 0):
    print(s + " is accepted")
else:
    print(s + " is not accepted")
    
