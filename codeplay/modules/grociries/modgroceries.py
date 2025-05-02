# grocery_module.py
def groceries_list():
    list= {
        "Rice": 2,
        "milk": 3,
        "chocolates":4,
        "corn flakes":5
    }
    prices={
        "Rice":90,
        "milk":40,
        "chocolates":50,
        "corn flakes":80
    }
    total = 0
    print("---- Grocery Bill ----")
    for item in list:
        qty = list[item]
        price = prices[item]
        item_total = qty * price
        print(f"{item}: {qty} x ₹{price} = ₹{item_total}")
        total += item_total

    print(f"\nTotal Bill: ₹{total}")