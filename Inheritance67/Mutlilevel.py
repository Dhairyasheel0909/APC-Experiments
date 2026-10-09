class parent:
    def info(self):
        print("Parent class")

class child1(parent):
    def child1(self):
        print("Child1 class")

class child2(child1):
    def child2(self):
        print("Child2 class")

obj=child2()

obj.info()
obj.child1()
obj.child2()

