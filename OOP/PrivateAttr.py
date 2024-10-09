class student:
    __course="BCA"  #private Attribute
    __semester=4 #private attribute
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def __Hello(self):   #private method
        print("Hello Bca student")
        print("hello, ",self.name)
    
    def print_PrivateAll(self):
        self.__Hello()  #calling private method
        print("semester:",self.__semester) #calling private attribute
        print("course:", self.__course)  #calling private attribute
    
s1=student("Ranjita", 9)

print(s1.print_PrivateAll())   #calling public method to access private attribute and method
print("Name:",s1.name)
print("RollNo:",s1.rollno)
