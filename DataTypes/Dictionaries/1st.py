#dictionary items are changeable, ordered and don't allow duplicate

mydictionary={
    "name": "Ranjita",
    "Age":18,
    "Gender": "Female",
    "Address": "Nuwakot", #here two address, but print last one 
    "Address": "kalanki",
    "Fav color":["Blue","Black"],
    "BCA":True
}
print(mydictionary)  #print all

print(mydictionary["Gender"]) #print only gender value i.e Female

print(type(mydictionary)) #check type

print(len(mydictionary))  #check length


#copy
#using copy() method
mydictionary2=mydictionary.copy()
print(mydictionary2)

#using dict() method
mydictionary3=dict(mydictionary)
print(mydictionary3)