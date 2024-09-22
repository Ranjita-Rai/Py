List=[ "Ranjita", "Sanjita", "Kriti", "Samana"]
NumList=[10,3,56,32,7,85]

#string concatination jastaiii
#List ma vako element pahila aauxa then numlist ma vako

#using (+) operator
JoinList=List+NumList   
print(JoinList)


#using append () ##append means add single elements to the end of the list
for i in NumList:
    List.append(i)
print(List)

print(" ")
#using extend () ##extend means add multiple elements at a time to the end of the list  
List.extend(NumList)
print(List)
