from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = [] # for storing new employees from the company

    def add_employee(self, newEmployee): # method to add the new employees into the empty list created above
        self.employees.append(newEmployee)

    def display_employees(self): # method for displaying the employees
        print("Current employees:")
        for i in self.employees:
            print(i.firstName, i.lastName)

    def pay_employees(self):
        print("Paying employees:")
        for i in self.employees:
            print("Payslip for:", i.firstName, i.lastName)
            print(f"Weekly amount: €{i.calculate_payslip():,.2f}")
            print("-------------------")


    
def main(): # create a new object based on Company class
    myCompany = Company()

    employee1 = SalaryEmployee("Sarah", "Hess", 50000)
    myCompany.add_employee(employee1)

    employee2 = HourlyEmployee("Lee", "Smith", 25, 50)
    myCompany.add_employee(employee2)

    employee3 = CommissionEmployee("Bob", "Brown", 30000, 5, 200)
    myCompany.add_employee(employee3)

    myCompany.display_employees()
    print("-------------------")
    myCompany.pay_employees()

main()