List=[ "Ranjita", "Sanjita", "Kriti", "Samana"]
NumList=[10,3,56,32,7,85]

#ascending order
List.sort()  #sorting in alphabetical order and Ascending order
print(List)

NumList.sort() #sorting in  ascending order
print(NumList)   


#descending order
List.sort(reverse=True)  #sorting in alphabetically but descending order
print(List)

NumList.sort(reverse=True)
print(NumList)  #sorting in descending order

NumList.sort(reverse=False)  #if we write reverse=false then sorting in ascending order, By default ascending hunxa
print(NumList)
