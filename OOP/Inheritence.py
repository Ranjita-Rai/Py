# parent class is being used to inherit the properties of the parent class
#child class  is inheriting the properties of the parent class

class parent:
    def __init__(self, name, address):
        self.name=name
        self.address=address

    def print(self):
        print(self.name, self.address)     

class child(parent):
    pass

obj=parent("Ranjita", "Nuwakot")
obj.print()