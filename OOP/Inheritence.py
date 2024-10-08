# parent class is being used to inherit the properties of the parent class
#child class  is inheriting the properties of the parent class

class parent:
    def __init__(self, name, address):  # constructor
        self.name=name 
        self.address=address

    def print(self): 
        print(self.name, self.address) 

class child(parent):   # child class is inheriting the properties of the parent class
    pass   #pass keyword is used to define a function or class without any code

obj=parent("Ranjita", "Nuwakot")   # creating an object of the parent class
obj.print()   # calling the method of the parent class



####QQ###
class car:
    color="black"
    @staticmethod
    def start(self):
        print("car started..")
    
    @staticmethod
    def stop(self):
        print("car stopped..")

class Toyota(car):
    def __init__(self, name):
        self.name=name

car1=Toyota("Fortuner")
car2=Toyota("pirus")
print(car1.start)
print(car1.name)
print(car2.name)
print(car1.color)
print(car2.color)