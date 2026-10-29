employee = {
    "name": input("Employee Name: "),
    "employee_id": input("Employee ID: "),
    "company": input("Company Name: "),
    "department": input("Department: "),
    "designation": input("Designation: "),
    "email": input("Email: "),
    "phone": input("Phone Number: "),
    "joining_date": input("Date of Joining: ")
}

print("\n--- Employee Details ---")
for key, value in employee.items():
    print(f"{key.title()}: {value}")
  