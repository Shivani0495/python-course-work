
import random

print("===== Welcome to Python Myntra =====")

users = []
cart = []
orders = []

categories = {
    "Men": {
        "T-Shirts": [{"id": 1, "name": "Nike Tee", "price": 899}, {"id": 2, "name": "Puma Tee", "price": 799}],
        "Jeans": [{"id": 3, "name": "Levis Jeans", "price": 1599}]
    },
    "Women": {
        "Dresses": [{"id": 4, "name": "Zara Dress", "price": 1299}],
        "Tops": [{"id": 5, "name": "H&M Top", "price": 799}]
    },
    "Kids": {
        "Shirts": [{"id": 6, "name": "Kids Shirt", "price": 499}]
    },
    "Home": {
        "Bedsheets": [{"id": 7, "name": "Floral Bedsheet", "price": 699}]
    },
    "Beauty": {
        "Lipstick": [{"id": 8, "name": "Maybelline Lipstick", "price": 299}]
    },
    "GenZ": {
        "Hoodies": [{"id": 9, "name": "Oversized Hoodie", "price": 999}]
    },
    "Studio": {
        "Activewear": [{"id": 10, "name": "Adidas Trackpants", "price": 1299}]
    }
}

# User login/registration
logged_in = False
current_user = None

while not logged_in:
    print("\n1. Register\n2. Login")
    choice = input("Select option: ")
    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        exists = any(user["username"] == username for user in users)
        if exists:
            
            print("Username already exists.")
        else:
            users.append({"username": username, "password": password})
            print("Registered! Please login.")
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                logged_in = True
                current_user = user
                print("Login successful! Welcome,", username)
                break
        else:
            print("Invalid credentials.")

# Menu loop
while True:
    print("\n===== Myntra Categories =====")
    print("1. Men")
    print("2. Women")
    print("3. Kids")
    print("4. Home")
    print("5. Beauty")
    print("6. GenZ")
    print("7. Studio")
    print("0. View Cart | 99. Checkout & Pay | 100. Logout")
    choice = input("Choose category (or option): ")

    if choice == "0":
        if cart:
            print("\n--- Cart Items ---")
            for item in cart:
                print(f"- {item['name']} | ₹{item['price']}")
        else:
            print("Cart is empty.")
    elif choice == "99":
        if not cart:
            print("Cart is empty.")
        else:
            total = sum(item["price"] for item in cart)
            print("\n--- Your Bill ---")
            for item in cart:
                print(f"- {item['name']} | ₹{item['price']}")
            print("Total amount: ₹", total)
            pay = input("Pay now? (yes/no): ")
            if pay.lower() == "yes":
                delivery = random.choice(["Raj", "Amit", "Rekha", "Shiva"])
                orders.append({"items": cart[:], "total": total, "delivery": delivery})
                print("Payment successful. Order placed!")
                print("Delivery assigned to:", delivery)
                cart.clear()
            else:
                print("Payment cancelled.")
    elif choice == "100":
        print("Logged out.")
        break
    elif choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected_cat = list(categories.keys())[int(choice) - 1]
        subcats = categories[selected_cat]

        print(f"\n--- {selected_cat} Subcategories ---")
        for idx, subcat in enumerate(subcats.keys(), 1):
            print(f"{idx}. {subcat}")
        sub_choice = int(input("Select subcategory: "))
        subcat_name = list(subcats.keys())[sub_choice - 1]

        print(f"\n--- {subcat_name} Products ---")
        items = subcats[subcat_name]
        for item in items:
            print(f"{item['id']} - {item['name']} | ₹{item['price']}")

        while True:
            action = input("Enter Product ID to add to cart (0 to go back, -ID to remove): ")
            if action == "0":
                break
            elif action.startswith("-"):
                remove_id = int(action[1:])
                found = False
                for i in range(len(cart)):
                    if cart[i]["id"] == remove_id:
                        print(cart[i]["name"], "removed from cart.")
                        del cart[i]
                        found = True
                        break
                if not found:
                    print("Item not found in cart.")
            else:
                prod_id = int(action)
                added = False
                for item in items:
                    if item["id"] == prod_id:
                        cart.append(item)
                        print(item["name"], "added to cart.")
                        added = True
                        break
                if not added:
                    print("Invalid product ID.")
    else:
        print("Invalid option.")
