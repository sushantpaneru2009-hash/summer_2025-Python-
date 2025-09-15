

def register():
    u = input("Username: ")
    p = input("Password: ")
    t = input("Type (buyer/seller): ")
    with open("users.txt", "a") as f:
        f.write(f"{u},{p},{t}")
    print("Registered!")

def login():
    u = input("Username: ")
    p = input("Password: ")
    with open("users.txt", "r") as f:
        for line in f:
            name, pwd, typ = line.strip().split(",")
            if u == name and p == pwd:
                print("Login successful!")
                return typ, u
    print("Login failed.")
    return None, None

def buyer():
    while True:
        c = input("1. View Products\n2. Buy Product\n3. Exit\nChoice: ")
        if c == "1":
            with open("products.txt", "r") as f:
                print(f.read())
        elif c == "2":
            print("Buying... (dummy)")
        else:
            break

def seller(user):
    while True:
        c = input("1. Add Product\n2. My Products\n3. Exit\nChoice: ")
        if c == "1":
            name = input("Product name: ")
            desc = input("Description: ")
            price = input("Price: ")
            with open("products.txt", "a") as f:
                f.write(f"{name},{desc},{price},{user}\n")
        elif c == "2":
            with open("products.txt", "r") as f:
                for line in f:
                    if line.strip().endswith(user):
                        print(line.strip())
        else:
            break

# Main
ch = input("1. Login\n2. Register\nChoice: ")
if ch == "2":
    register()
    typ, user = login()
elif ch == "1":
    typ, user = login()
else:
    typ = None

if typ == "buyer":
    buyer()
elif typ == "seller":
    seller(user)