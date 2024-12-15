name = input("Enter your name: ")
IsEnrolled = input("Are you currently enrolled in DLL (yes / no):   ")
if IsEnrolled.lower() == "yes":
#Age of the student
    print(f"Hi {name}, Welcome to the DLL scholarship grant system")
    age = eval(input("Enter your age: "))

    if age >= 18 and age <= 35:
        print("Your age complied with the age requirement")

        #Grades of the students
        grades = eval(input("Enter your last GNA: "))
        
        if grades >= 85 and grades <= 100:
            print("Your Last GWA passed the requiremnts")

            is4ps = input("Are your family a member of Apa (yes / no): ")

            if is4ps.lower() == "yes":
                print("Congratulation you passed the granted a scholarship")
            else:
                print("Sorry on 4ps is allowed for DLL scholarship")
        else:
            print(("Sorry you didn't passed the GWA requirements"))
    else:
        print("Sorry you didn't passed the age requirements") 
else:
    print("Thank you for using the system")