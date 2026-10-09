
class child1:
    def child1(self):
        print("Child1 class")

class child2:
    def child2(self):
        print("Child2 class")

class parent(child1,child2):
    def info(self):
        print("Parent class")

obj=parent()

obj.child1()
obj.child2()
obj.info()