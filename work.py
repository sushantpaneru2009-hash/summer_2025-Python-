USER_FILE = "users.json"
PRODUCT_FILE = "products.json"

# Load data
def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Register user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    usertype = input("Enter user type (buyer/seller): ")

    users = load_data(USER_FILE)
    if any(u['username'] == username for u in users):
        print("Username already exists.")
        return

    users.append({'username': username, 'password': password, 'usertype': usertype})
    save_data(USER_FILE, users)
    print("Registered successfully.")

# Login user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    users = load_data(USER_FILE)
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful.")
            return user
    print("Invalid credentials.")
    return None

# Buyer options
def buyer_menu():
    print("1. Get Products\n2. Buy Product")
    choice = input("Enter choice: ")
    products = load_data(PRODUCT_FILE)
    if choice == "1":
        for p in products:
            print(p)
    elif choice == "2":
        pid = input("Enter product ID to buy: ")
        print("Product bought (not actually implemented).")

# Seller options
def seller_menu(username):
    print("1. Add Product\n2. Get My Products")
    choice = input("Enter choice: ")
    products = load_data(PRODUCT_FILE)
    if choice == "1":
        name = input("Enter product name: ")
        desc = input("Enter description: ")
        price = input("Enter price: ")
        product = {
            "id": len(products)+1,
            "name": name,
            "description": desc,
            "price": price,
            "seller": username
        }
        products.append(product)
        save_data(PRODUCT_FILE, products)
        print("Product added.")
    elif choice == "2":
        for p in products:
            if p['seller'] == username:
                print(p)

# Main logic
def main():
    action = input("Login or Register? ").lower()
    if action == "register":
        register()
    elif action == "login":
        user = login()
        if user:
            if user['usertype'] == 'buyer':
                buyer_menu()
            elif user['usertype'] == 'seller':
                seller_menu(user['username'])