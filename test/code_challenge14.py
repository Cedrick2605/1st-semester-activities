#BANK SIMULATION PROGRAM 
#CREATE ACCOUNT
#DEPOSIT
#WITHDRAW
#CHECK BALANCE 

#Ask the user to create an account,
#After she/he will need to make an intial deposit 
#Before depositing display the filipino denominations of the amount 
#After display the denomination proceed to deposit said amount 
#if user wants to withdraw, ask for the amount to withdraw,
#withdrawal amount should not be less the current balance. 
#After withdrawal show the current balance. 
#Current balance option would only display current balance
#Everything should be repeated until user opts out
dept = 0

# Deposit
def withdraws():
    global dept
    withdraw = eval(input("Enter an amount you want to withdraw: "))
    if withdraw > dept:
        print("Insufficient balance")
    elif withdraw <= 0:
        print("Invalid amount")
    else:
        dept -= withdraw
        print(f"You have withdrawn an amount of: ₱{withdraw}.")
        print(f"Your current balance is: ₱{dept}.")

def balances():
    print(f"Your current balance is: ₱{dept}")

def denomination():
    global dept
    #denominations
    one_thousand = dept // 1000
    onethousand_change = dept % 1000
    five_hundred = onethousand_change // 500
    fivehundred_change = onethousand_change % 500
    two_hundred = fivehundred_change // 200
    twohundred_change = fivehundred_change % 200
    one_hundred = twohundred_change // 100
    onehundred_change = twohundred_change % 100
    fifthy = onehundred_change // 50
    fifthy_change = onehundred_change % 50
    twenthy = fifthy_change // 20
    twenthy_change = fifthy_change % 20
    tenth = twenthy_change // 10
    tenth_change = twenthy_change % 10
    fifth = tenth_change // 5
    fifth_change = tenth_change % 5
    one = fifth_change // 1

    print(f"\t{one_thousand} - 1000 \n\t{five_hundred} - 500\n\t{two_hundred} - 200\n\t{one_hundred} - 100\n\t{fifthy} - 50\n\t{twenthy} - 20\n\t{tenth} - 10\n\t{fifth} - 5\n\t{one} - 1")

def deposits():
    global dept
    deposit = eval(input("Enter an amount you want to deposit: "))
    if deposit <= 0:
        print("Invalid deposit amount")
    else:
        dept += deposit
        print(f"You have deposited ₱{deposit}.")
        print(f"Your current balance is: ₱{dept}.")

def exit_program():
    print(f"Thank you, {name}. Have a good day!")

#Intro
print("\n----- Welcome to the bank simulation program -----")
print("--- Please create an account ---\n")

name = input("Enter a name to create an account: ")
print(f"Hi, {name}, you have successfully created an account.")
dept = eval(input("Enter an amount you will deposit: "))

print("\n--- Filipino denomination ---\n₱1000\n₱500\n₱200\n₱100\n₱50\n₱20\n₱10\n₱5\n₱1")
print(f"\nYou deposited an amount of ₱{dept}")

#Loop
dup = True
while dup:
    con = input("\nDo you want to deposit, withdraw, check balance, or check Filipino denomination? (deposit/withdraw/check/denomination/exit): ").lower()
    if con == "deposit":
        deposits()
    elif con == "withdraw":
        withdraws()
    elif con == "check":
        balances()
    elif con == "denomination":
        denomination()
    elif con == "exit":
        exit_program()
        dup = False
        break
    else:
        print("Invalid option. Please try again.")