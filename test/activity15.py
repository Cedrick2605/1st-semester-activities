# tirangle horizontal
num=eval(input("Enter number of triangles:  "))
for x in range(1,6):
    for a in range(1,num+1):
        for y in range(1,x+1):
            print("*",end=" ")
        for z in range(6,x,-1):
            print(" ",end=" ")
        print(end=" ")
    print()
import os
repeat = True
num = 0
while repeat == True:
    tel = input("Do you want to make more triangles (yes/no):   ")

    if tel.lower() == "no":
        print("Loop has ended")
        repeat = False
        break

    elif tel.lower()=="yes":
        os.system('cls')
        num+=1
        num=eval(input("Enter number of triangles:  "))
        for x in range(1,6):
            for a in range(1,num+1):
                for y in range(1,x+1):
                    print("*",end=" ")
                for z in range(6,x,-1):
                    print(" ",end=" ")
                print(end=" ")
            print()
            continue
    else:
        print("Invalid")
        print("Please type only yes or no")
        continue