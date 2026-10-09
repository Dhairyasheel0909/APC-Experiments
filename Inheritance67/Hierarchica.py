class parent:
    def info(self):
        print("Parent class")

class child1(parent):
    def child1(self):
        print("Child1 class")

class child2(parent):
    def child2(self):
        print("Child2 class")

obj1=child1()
obj1.info()
obj1.child1()

obj2=child2()
obj2.info()
obj2.child2()