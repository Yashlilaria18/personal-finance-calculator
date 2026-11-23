#Project 1

        #Personal info.
employee_name = input("Enter your name : ")
print(f"{employee_name}")
age = int(input("Enter your age : "))
print(f"{age}")
city = input("Enter your city : ")
print(f"{city}")
emp_id = int(input("Enter your employee id : "))
print(f"{emp_id}")
is_employee_permanent = bool(input("Are you permanent employee? (yes/no) : ").lower() == "yes")
print(f"{is_employee_permanent}")

        # salary calculation
basic_salary = float(input("Enter your basic salary : "))
print(f"{basic_salary}")
hra_20 = ( basic_salary *20/100)
print(f"{hra_20}")
da_10 = (basic_salary * 10/100)
print(f"{da_10}")
pf_12 = (basic_salary * 12/100)
print(f"{pf_12}")
gross_salary = basic_salary + hra_20 + da_10
print(f" Gross salary = {gross_salary}")
net_salary = gross_salary - pf_12
print(f"Net salary = {net_salary}")

        #Monthly Expense Calculator
rent  = float(input("Enter your monthly rent : "))
print(f"Monthly rent = {rent}")
food = float(input("Enter your monthly food expense : "))
print(f"Monthly food expenses = {food}")
gym = float(input("Enter your monthly gym expense : "))
print(f"Monthly gym expenses = {gym}")
travel = float(input("Enter your monthly travel expense : "))
print(f"Monthly travel expenses = {travel}")
other_expenses = float (input("Enter your other monthly expenses : "))
print(f"Other monthly expenses = {other_expenses}")

total_monthly_expenses = rent + food + gym + travel + other_expenses
print(f"Your total monthly expenses are : {total_monthly_expenses}")
monthly_savings = net_salary - total_monthly_expenses
print(f"Your monthly savings are : {monthly_savings}")
annual_savings = monthly_savings * 12
print(f"Your annual savings are : {annual_savings}")
