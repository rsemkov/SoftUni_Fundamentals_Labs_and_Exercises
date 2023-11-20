company_users = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_users.keys():
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

for company, employees in company_users.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")