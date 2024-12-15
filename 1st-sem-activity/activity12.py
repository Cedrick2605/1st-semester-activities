for x in range(1,7):
    for y in range(x,7):
        print(" ",end=" ")
    for a in range(0,x):
        print("*",end=" ")
    for b in range(1,x):
        print("*",end=" ")
    print()

for x in range(1,6):
    for y in range(0,x+1):
        print(" ",end=" ")
    for a in range(x,6):
        print("*",end=" ")
    for b in range(x,5):
        print("*",end=" ")
    print()