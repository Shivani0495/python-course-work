# k.shivani (PFS-22)

# 1. Hospital ID (int)
hospital_id = int(input("Enter Hospital ID: "))

# 2. Hospital Name (str)
hospital_name = input("Enter Hospital Name: ")

# 3. Consultation Fee (float)
consultation_fee = float(input("Enter Consultation Fee (₹): "))

# 4. Departments Available (list)
dept_input = input("Enter Departments Available (comma-separated): ")
departments = [d.strip() for d in dept_input.split(",")]

# 5. Bed Availability (tuple) – Total Beds and Occupied Beds
total_beds = int(input("Enter Total Beds: "))
occupied_beds = int(input("Enter Occupied Beds: "))
bed_status = (total_beds, occupied_beds)

# 6. Insurance Discount (float)
insurance_discount = float(input("Enter Insurance Discount Percentage: "))


# 7. Facilities (set)
facilities_input = input("Enter Facilities (comma-separated): ")
facilities = set(f.strip() for f in facilities_input.split(","))

# 8. Branch Info (dict)
branch_name = input("Enter Branch Name: ")
branch_contact = input("Enter Branch Contact Number: ")
branch_location = input("Enter Branch Location: ")
branch_info = {
    "name": branch_name,
    "contact": branch_contact,
    "location": branch_location
}


# **Display Hospital Details Using Different Formatting Methods***

print("\n" + "-"*45)
print("HOSPITAL INFORMATION FORMATTED OUTPUT")
print("-"*45)

# 1. Using Comma Separation (sep=',')
print("Hospital ID, Name, Fee:", hospital_id, hospital_name, consultation_fee, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Insurance Discount Available: %.2f%%" % insurance_discount)

# 3. Using f-strings
print(f"Hospital Name: {hospital_name}")
print(f"Consultation Fee: ₹{consultation_fee}")
print(f"Insurance Discount: {insurance_discount}%")
print(f"Bed Status: {bed_status[0]} Total | {bed_status[1]} Occupied")

# 4. Using .format() method
print("Branch Details: Name - {}, Contact - {}, Location - {}".format(
    branch_info['name'], branch_info['contact'], branch_info['location']
))

print("\nDepartments Available:", departments)
print("Facilities:", facilities)
