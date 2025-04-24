import json

flights = [
    {"number": "AI101", "destination": "New York", "time": "10:30"},
    {"number": "BA202", "destination": "London", "time": "14:15"},
    {"number": "QR303", "destination": "Doha", "time": "22:45"},
    {"number": "EK404", "destination": "Dubai", "time": "09:00"},
    {"number": "LH505", "destination": "Frankfurt", "time": "12:50"},
]

def add_flight():
    number = input("Enter Flight Number: ")
    destination = input("Enter Destination: ")
    time = input("Enter Departure Time (HH:MM): ")
    for f in flights:
        if f['number'] == number:
            print("⚠ Flight with this number already exists!\n")
            return
    flights.append({"number": number, "destination": destination, "time": time})
    print("✅ Flight added successfully!\n")

def view_flights():
    if not flights:
        print("⚠ No flights available.\n")
        return
    print("\n🛫 List of Flights:")
    for f in flights:
        print(f"Flight No: {f['number']} | To: {f['destination']} | At: {f['time']}")
    print()

def search_flight():
    number = input("Enter Flight Number to search: ")
    found = False
    for f in flights:
        if f['number'] == number:
            print(f"✅ Found: {f}")
            found = True
            break
    if not found:
        print("❌ Flight not found.\n")

def delete_flight():
    number = input("Enter Flight Number to delete: ")
    index = -1
    for i in range(len(flights)):
        if flights[i]['number'] == number:
            index = i
            break
    if index != -1:
        del flights[index]
        print("🗑 Flight deleted successfully!\n")
    else:
        print("❌ Flight not found.\n")

def update_flight():
    number = input("Enter Flight Number to update: ")
    for f in flights:
        if f['number'] == number:
            new_dest = input("Enter new Destination: ")
            new_time = input("Enter new Departure Time (HH:MM): ")
            if new_dest:
                f['destination'] = new_dest
            if new_time:
                f['time'] = new_time
            print("✏ Flight updated successfully!\n")
            return
    print("❌ Flight not found.\n")

def save_to_file():
    with open("flights.json", "w") as file:
        json.dump(flights, file)
    print("💾 Flights saved to file.\n")

def load_from_file():
    global flights
    try:
        with open("flights.json", "r") as file:
            flights = json.load(file)
        print("📂 Flights loaded from file.\n")
    except FileNotFoundError:
        print("❌ No saved file found.\n")

def menu():
    while True:
        print("\n--- Airport Management System ---")
        print("1. Add Flight")
        print("2. View All Flights")
        print("3. Search Flight")
        print("4. Delete Flight")
        print("5. Update Flight")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            add_flight()
        elif choice == '2':
            view_flights()
        elif choice == '3':
            search_flight()
        elif choice == '4':
            delete_flight()
        elif choice == '5':
            update_flight()
        elif choice == '6':
            save_to_file()
        elif choice == '7':
            load_from_file()
        elif choice == '8':
            print("👋 Exiting system.")
            break
        else:
            print("⚠ Invalid choice. Try again.")

menu()