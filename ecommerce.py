# user_details=[{"username":"sushant"},{"username":"pawan"},{"username":"sandesh"}]
# # json data 

# for i in range(len(user_details)):
#     if user_details[i]["username"] == "Sushant":
#         print("user exists") 
        
# user_length= len(user_details)


# product_details=[{
#     "name":"",
#     "description":"",
#     "price":""
# }]

# User data stored in dictionaries
# user_credentials = {
#     "neymar": "santodh fc",
#     "messi": "intermiami",
#     "ronaldo": "alnasar"
# }

# user_balances = {
#     "neymar": 111000.0,
#     "messi": 1500.0,
#     "ronaldo": 5000.0
# }

# # ---------------- Function to Register ----------------
# def register():
#     print(" Register ")
#     username = input("Choose a username: ").strip()
    
#     if username in user_credentials:
#         print("Username already exists! Try logging in instead.")
#     else:
#         f = open("user_credintial.txt",'a')
#         f.write(f"{username},{password}")
#         return 

#     password = input("Choose a password: ").strip()
    
#     try:
#         starting_balance = float(input("Enter starting balance: Rs"))
#         if starting_balance < 0:
#             print("Balance cannot be negative.")
#             return
#     except ValueError:
#         print("Invalid amount. Please enter a number.")
#         return

#     # Save new user
#     user_credentials[username] = password
#     user_balances[username] = starting_balance
#     print(f"User '{username}' registered successfully!")

# # ---------------- Function to Login ----------------
# def login():
#     print("--- Login ---")
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ").strip()

#     if username in user_credentials and user_credentials[username] == password:
#         print("Login Successful!")
#     elif username not in user_credentials:
#         print(user_name_not_registered)
        
#     else:
#         print("Invalid username or password. Try again.")
#         return None

# # ---------------- Show User Details ----------------
# def show_details(username):
#     print(f"Account Details for {username} ")
#     print(f"Balance: Rs{user_balances[username]:}")

# # ---------------- Add Balance ----------------
# def add_balance(username):
#     try:
#         amount = float(input("Enter amount to add: Rs"))
#         if amount <= 0:
#             print("Amount must be greater than 0.")
#             return
#         user_balances[username] += amount
#         print(f"Updated Balance: Rs{user_balances[username]:}")
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# # ---------------- Main Program ----------------
# while True:
#     print(" Welcome to Simple Bank ***")
#     print("1. Login")
#     print("2. Register")
#     print("3. Exit")
    
#     main_choice = input("Enter your choice (1/2/3): ").strip()

#     if main_choice == '1':
#         username = login()
#         if username:
#             # Logged-in menu
#             while True:
#                 print("Logged In Menu ---")
#                 print("1. Show Account Details")
#                 print("2. Add Balance")
#                 print("3. Logout")

#                 user_choice = input("Enter your choice (1/2/3): ").strip()

#                 if user_choice == '1':
#                     show_details(username)
#                 elif user_choice == '2':
#                     add_balance(username)
#                 elif user_choice == '3':
#                     print("Logging out...")
#                     break
#                 else:
#                     print("Invalid choice. Please enter 1, 2 or 3.")
#     elif main_choice == '2':
#         register()
#     elif main_choice == '3':
#         print("Thank you for using Simple Bank. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2 or 3.")

choice = input("login" or "register" )
def register():
    username: input('enter username')
    pasword = input('password:')
    file = {username:password}
    f = open()