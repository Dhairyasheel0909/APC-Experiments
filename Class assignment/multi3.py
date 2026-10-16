class Person:
    def person_info(self,name,age):
        self.name=name
        self.age=age

    
        print("Person Name: ",self.name)
        print("Age: ",self.age)


class Employee(Person):
    def employee_info(self,id,salary):
        self.id=id
        self.salary=salary

    
    
        print("Employee ID:",self.id)
        print("Salary: ",self.salary)


class Manager(Employee):
    def manager_info(self,dept,size):
        self.dept=dept
        self.size=size

    
        print("Department: ",self.dept)
        print("Team Size: ",self.size)


obj = Manager()

obj.person_info("Dhairyasheel",21)
obj.employee_info(109,5000000)
obj.manager_info("Software",8)
