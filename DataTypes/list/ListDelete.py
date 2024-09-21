####delete##
List=[ "Ranjita", "Sanjita", "Kriti", "Samana"]
#using remove()
'''List.remove("Ranjita")  #delete ranjita from the list
print(List)'''



#using pop ()
'''
List.pop(1) #delete sanjita from list(sanjita at index1 )
print(List)

List.pop() #delete the last element from list
print(List)
'''


#using del keyword to delete list (specific index as well as entire list)
'''del List()
print(List) #this will cause an error because you have succsesfully deleted "list".

del List[2] #delete index 2 element from list
print(List)
'''


#using clear () to delete element
'''
List.clear() #delete all elements from list
print(List)'''
