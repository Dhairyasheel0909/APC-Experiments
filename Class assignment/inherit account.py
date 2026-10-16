class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def info(self, employee_id, salary):  
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        self.display_person_info()  


emp1 = Employee("Dhairyasheel", 21)
emp1.info(109,500000)
emp1.display_employee_info()