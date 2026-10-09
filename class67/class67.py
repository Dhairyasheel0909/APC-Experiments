class student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Roll No. : ",self.roll)

s=student("Dhairyasheel",21,67)
s.display()  