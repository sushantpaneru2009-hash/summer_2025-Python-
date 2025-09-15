# user_detail = {"neymar":"njr.np","messi":"msi","ronaldo":"cr7"}
# balance = {"neymar":20000,"messi":23000,"ronaldo":6500}

# username = input("username:")
# password = input("password:")

# if user_detail == password:
#     print("login successfully")


# Main program loop
# while True:
user_credentials = {
    "neymar": [{"santos fc":"brazil","argentina":["europe","asia","africa"]},"barcelona"],
    "messi": "intermiami",
    "ronaldo": "alnasar"
}

print(user_credentials["neymar"][0]["argentina"][2])

# output -> europe

# user_balances = {
#     "neymar": 111000.0,
#     "messi": 1500.0,
#     "ronaldo": 5000.0
# }

# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
    
#     if username in user_credentials and user_credentials[username] == password:
#         print("Login Successful!")
#         return username
#     else:
#         print("Invalid username or password. Try again.")
#         return None  # Return None on failure

# def show_details(username):
#     print(f"--- Account Details ---")
#     print(f"Username: {username}")
#     print(f"Balance: Rs{user_balances[username]:.2f}")

# def add_balance(username):
#     try:
#         amount = float(input("Enter amount to add: Rs"))
#         if amount <= 0:
#             raise ValueError("Amount must be positive.")
#         user_balances[username] += amount
#         print(f"Updated Balance: Rs{user_balances[username]:.2f}")
#     except ValueError as e:
#         print(f"Error: {e}")

# # Main program loop
# while True:
#     username = login()
#     if username:
#         while True:
#             print("\nChoose an option:")
#             print("1. Show Details")
#             print("2. Add Balance")
#             print("3. Logout")
            
#             choice = input("Enter your choice (1/2/3): ")

#             if choice == '1':
#                 show_details(username)
#             elif choice == '2':
#                 add_balance(username)
#             elif choice == '3':
#                 print("Logging out...\n")
#                 break
#             else:
#                 print("Invalid choice. Try again.\n")

#     try_again = input("Do you want to try logging in again? (yes/no): ").strip().lower()
#     if try_again != 'yes':
#         print("Exiting the system. Goodbye!")
#         break
