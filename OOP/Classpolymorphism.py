class BCA:
    def __init__(self, name, rollno):
        self.name=name
        self.rolllno=rollno
    
    def print(self):
        print("Hello BCA students")

class BBM:
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno
    
    def print(self):
        print("Hello BBM students")

class BBA:
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno
    
    def print(self):
        print("Hello BBA students")
BCA1=BCA("Sumana", 13)
BBM1=BBM("Rahul", 14)
BBA1=BBA("Sanjeet", 15)

for x in (BCA1, BBM1, BBA1): 
  x.print()

print(BCA1.name)
print(BCA1.rolllno)