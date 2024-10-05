#create class using class keyword
class newclass:
    a=5
    b=10
print(newclass) #output: <class '__main__.newclass'>

print(newclass.a) #print value of a


#creating Object
obj=newclass()
print(obj.b) 

#using __init__()
# #All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
  def __init__(person, name, address):
    person.name = name
    person.address = address

obj = Person("Sanjana", "Ktm")

print(obj.name)
print(obj.address)
