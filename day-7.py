
#  Requirement 
# if the age of the user is greater than or equal to 18
#  check if the user has concert ticket
# if the user has concert ticket  print then print you are not allowded to enter
# if age of user is less than 18:
# print you are underage

# age =  20 
# concert_ticket = True
# if age >= 18:
#     if concert_ticket:
#         print("you are allowed to enter")
#     else:
#     int("you are not allowed to enter <=18
# elif a
    
    
age = int(input("What is your age?"))

if age >= 18:
    has_license = input("Do you have a driving license? (yes/no): ")
    if has_license == "yes":
        print("Great! Drive safe.")
    else:
        print("You should consider getting one.")
else:
    wants_license = input("Do you want a driving license? (yes/no): ")
    if wants_license == "yes":
        print("You will be eligible soon. Start learning")
age = int(input("Enter your age: "))





marks =int(input("what is the obtained marks?"))
if marks>50:
    if marks >= 80:
        print("Grade A")
    elif marks >= 65:
        print("Grade B")
    else :
         print("Grade C ")
else:
    print("Failed")