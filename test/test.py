# name = input("Enter your name :  ")
# purchase = input("Did you purchase a grocery today (yes / no) : ")

# if purchase.lower() == "yes":
#     whatitem = input("What did you purchase :    ")
#     price = eval(input("Enter the product price :  "))
#     age = eval(input("Enter your age :  "))
#     payment = eval(input("Enter the amount of your payment :    "))

#     #Taxed
#     taxed = price * 0.123
#     taxed2 = price + taxed
#     #Change
#     change = payment - taxed2
#     if change <= 0:
#         change = 0
#     #output1
#     if price <= 4000 and age <= 60 and age <= 150:
#         print(f"Hi {name}, you bought {whatitem} with the price of {round(taxed2, 2)}")
#         print(f"The amount of the change is : {round(change, 2)}")


#     elif price >= 4000 and age <= 60 and age <= 150:
#         #discounted
#         discount = price * 0.038
#         discount2 = price - discount
#         #change
#         change2 = payment - discount2
#         if change2 <= 0:
#             change2 = 0
#         #output2
#         print(f"Hi {name}, you bought {whatitem} with the price of {round(discount2, 2)}")
#         print(f"The amount of the change is : {round(change2, 2)}")


#     elif age >= 60 and age <= 150 and price <= 4000:
#         #discounted
#         discount3 = taxed2 * 0.123
#         discount4 = taxed2 - discount3
#         #change
#         change3 = payment - discount4
#         if change3 <=0:
#             change3 = 0
#         #output3
#         print(f"Hi {name}, you bought {whatitem} with the price of {round(discount4, 2)}")
#         print(f"The amount of the change is : {round(change3, 2)}")
    

#     elif age >= 60 and age <= 150 and price >= 4000:
#         #discounted
#         discount5 = price * 0.038
#         discount6 = price - discount5
#         discount7 = discount6 * 0.123
#         discount8 = discount6 - discount7
#         #change
#         change4 = payment - discount8
#         if change <= 0:
#             change = 0
#         #output4
#         print(f"Hi {name}, you bought {whatitem} with the price of {round(discount8, 2)}")
#         print(f"The amount of the change is : {round(change4, 2)}")
#     else:
#         print("Invalid")
# if purchase == "no":
#     print("Okay, Have a nice day :)")
# else:
#     print("Invalid")




dept = 0
print("\nWelcome")
print("Please create an account\n")

name = input("Enter a name to create an account: ")
print(f"Hi, {name}, you have successfully created an account.")

#Deposit
dept = eval(input("Enter an amount you will deposit: "))

#Denominations
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

print(f"Hi {name}, your deposit amount breakdown in PHP denomination is as follows:")
print(f"\t{one_thousand} - 1000 \n\t{five_hundred} - 500\n\t{two_hundred} - 200\n\t{one_hundred} - 100\n\t{fifthy} - 50\n\t{twenthy} - 20\n\t{tenth} - 10\n\t{fifth} - 5\n\t{one} - 1")

print(f"\nYou deposited an amount of {dept}")

#Loop
while True:
    con = input("\nDo you want to withdraw or check balance? (withdraw/check/exit): ")
    if con == "withdraw":
        withdraw = eval(input("Enter an amount you want to withdraw: "))
        if withdraw > dept:
            print("Insufficient balance")
        elif withdraw <= 0:
            print("Invalid")
        else:
            dept -= withdraw
            print(f"You have withdrawn an amount of:    {withdraw}.")
            print(f"Your current balance is:    {dept}.")
    elif con == "check":
        print(f"Your current balance is:    {dept}")
    elif con == "exit":
        print(f"Thank you, {name}, I hope you having a good day!")
        break
    else:
        print("Invalid. Choose (withdraw, check, or exit)")


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

    # if con == "withdraw":
    #     withdraw = eval(input("Enter an amount you want to withdraw: "))
    #     if withdraw > dept:
    #         print("Insufficient balance")
    #     elif withdraw <= 0:
    #         print("Invalid")
    #     else:
    #         dept -= withdraw
    #         print(f"You have withdrawn an amount of:    {withdraw}.")
    #         print(f"Your current balance is:    {dept}.")
    # elif con == "check":
    #     print(f"Your current balance is:    {dept}")
    # elif con == "exit":
    #     print(f"Thank you, {name} I hope you having a good day!")
    #     break
    # else:
    #     print("Invalid. Choose (withdraw, check, or exit)")
    #     continue
