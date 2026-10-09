class student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Roll No. : ",self.roll)

    def result(self,marks,totalmarks):
        percentage=(marks*100)/totalmarks
        print("Percentage : ",percentage)

    def __del__(self):
        print("Destructor")

s1=student("Dhairyasheel",21,67)
s1.display()  
s1.result(145,200)

s2=student("Vivek",25,69)
s2.display()  
s2.result(165,200)
del s1