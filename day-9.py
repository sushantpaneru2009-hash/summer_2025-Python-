# user_name = ["neymar","sachin","messi","virat"]
# input_username = input("enter your username?")
# if input_username  not in user_name:
#     print("invalid username")
# else : 
#     print("welcome and thanks for joining with us")
   
   
# user_info = {
#     "neymar": "psg",
#     "messi": "inter miami",
#     "vinicius": " real madrid",
#     "yamal": "barcelona"
# }

# input_username = input("enter your username?")
# if input_username in user_info:
#     print(f'wlcome {input_username},you are in the system')
# else:
#     print("invalid username")
# login_username = input("enter your username ?")
# login_password = input("enter your password ?")
# if login_username in user_info:
#     if login_password == user_info[login_username]:
#             print("login successful")
# else:
#     print("invalid username or password")

# exceptional error : error that occurs during the execution of the program
a = 10
try:
    data= int(input("enter a number?"))
    print(a-data)
except:
    print("there is an error")
finally:
    print("execution completed")