class parent:
    def info(self):
        print("Parent class")

class child1(parent):
    def child1(self):
        print("Child1 class")

class child2(parent):
    def child2(self):
        print("Child2 class")

class grandfather(child1,child2):
    def grand(self):
        print("Grandfather class")

obj=grandfather()
obj.grand()
obj.info()
obj.child1()
obj.child2()
