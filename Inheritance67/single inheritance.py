class parent:
    def info(self):
        print("Parent class")

class child(parent):
    def display(self):
        print("Child class")

obj=child()

obj.info()
obj.display()