newDict={
    'college':'Nepalaya',
    'student':1500,
    'BCA': True,
    'Csit':True,
    'BIT':False,
    'location':'kalanki'
}
#using pop() method
newDict.pop('location') #remove location
print(newDict)


#using popitem() method
newDict.popitem()  #remove last elements
print(newDict)




#using del keyword
del newDict['student'] #remove student
print(newDict)


#using clear() method
newDict.clear()  #delete all dictionery
print(newDict)  #output: {}

#using del keyword to remove all elements
del newDict #del keyword delete/remove whole dictionary
#this will cause an error because "newDict" no longer exists.
print(newDict)