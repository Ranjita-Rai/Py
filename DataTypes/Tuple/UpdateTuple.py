#Tuples are unchangeable, or immutable but we can convert the tuple into a list, we can change the list, and convert the list back into a tuple.

Tuple=("Apple" , "Mango", "Banana")
NewTuple=list(Tuple)  #convert Tuple into list and assign with NewTuple variable
NewTuple[1]="Orange"  #add orange in 1st index , i.e . Mango's position
Tuple=tuple(NewTuple) #covert NewTuple (list) into tuple and assign with Tuple variable 
print(Tuple) #Orange replace  Mango in Tuple