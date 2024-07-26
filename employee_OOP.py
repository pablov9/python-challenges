class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class SalaryEmployee(Employee):
    def __init__(self, firstName, lastName, salary):
        # self.firstName = firstName // not needed as we are using inheritance
        # self.lastName = lastName // not needed as we are using inheritance 
        super().__init__(firstName, lastName)
        self.salary = salary

    def calculate_payslip(self):
        return self.salary/52
    
class HourlyEmployee(Employee):
    def __init__(self, firstName, lastName, weeklyHours, hourlyRate):
        super().__init__(firstName, lastName)
        self.weeklyHours = weeklyHours
        self.hourlyRate = hourlyRate

    def calculate_payslip(self):
        return self.weeklyHours*self.hourlyRate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, firstName, lastName, salary, salesNumber, commissionRate):
        super().__init__(firstName, lastName, salary)
        self.salesNumber = salesNumber
        self.commissionRate = commissionRate
    
    def calculate_payslip(self):
        regularSalary = super().calculate_payslip()
        totalCommission = self.salesNumber*self.commissionRate
        return regularSalary + totalCommission


