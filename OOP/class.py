#create class using class keyword
class newclass:
    a=5
    b=10
print(newclass) #output: <class '__main__.newclass'>

print(newclass.a) #print value of a


#creating Object
obj=newclass()
print(obj.b) 

#using __init__() function
# #All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address

obj = Person("Sanjana", "Ktm")

print(obj.name)
print(obj.address)

#Using __str__()function
#The __str__() function is used to return a string representation of the object.
class student:
   def __init__(self,id,name,address,age):
      self.id=id
      self.name=name
      self.address=address
      self.age=age
   def __str__(self):
      return f"{self.id} {self.name} {self.address} {self.age}"
obj=student(1,"Sanjana","Ktm",20)
print(obj)



##Q.. 
class bank_Acc:
   def __init__(self, Acc_No, Balance):
      self.Account_No=Acc_No
      self.balance=Balance
   
   def debit(self, amount):
      self.balance-=amount
      print(f"Debit: ${amount}. Remaining balance is Rs.{self.balance}")
    
   def credit(self, amount):
      self.balance+=amount
      print(f"Credited: ${amount}. Remaining balance is Rs.{self.balance}")
account_1= bank_Acc(1297352, 1500)
account_1.debit(1000)
account_1.credit(20000)