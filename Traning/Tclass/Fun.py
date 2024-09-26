
'''import math
from Function import find_square   ##function file ko find_square lao=i import garxa
square=math.sqrt(5)
print(square)
find_square(7)'''


'''def main():
    print("Square of Num")
    find_square(6)
    print("Hello, World!")
if __name__=="__main__":
    main()'''

'''def add(*numbers):
    
    for num in numbers:
        print(num)
    

add(1,5,6,7,3,5)

def Prog(*args):
    for arg in args:
        print(arg)
Prog("Hello","My", "name","is","Ranjita", "Rai")
'''

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        print("%s==%s" % (key,value))
greet(name="Ranzee",greeting="Hello")

