num = eval(input("enter you number: "))
fact = 1
for x in range(num,0,-1):
    print(x)
    fact * x
print(f"{fact}")