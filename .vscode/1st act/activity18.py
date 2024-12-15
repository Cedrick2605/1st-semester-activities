#function for calculating factorial

def factorial(number):
    """This funtion is for calculating factorial"""
    fact = 1
    for x in range(number,0,-1):
        fact *= x
    return fact

# factorial(5)
# help(factorial)
# help (print)