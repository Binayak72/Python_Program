import random


def get_employee_details():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")

    # Flight assignment is done randomly
    assigned_flight = random.choice(['Air India', 'Vistara Airlines', 'Indigo'])

    return {
        'empid': emp_id,
        'name': name,
        'position': position,
        'assigned_flight': assigned_flight
    }


def main():
    employees = []

    num_employees = int(input("Enter the number of employees: "))

    for _ in range(num_employees):
        employee_details = get_employee_details()
        employees.append(employee_details)

    print("\nEmployee Information:")
    for employee in employees:
        print(
            f"Employee ID: {employee['empid']},"
            f"Name: {employee['name']}, "
            f"Position: {employee['position']}, "
            f"Assigned Flight: {employee['assigned_flight']}")


if __name__ == "__main__":
    main()
