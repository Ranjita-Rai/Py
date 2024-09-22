newTuple=("Rawzu", "Sabita", "Sanjita","Anamika")
print(newTuple[2])  #print index 2 element
print(newTuple[-1])  #-1 refers to the last element i.e anamika
print(newTuple[0:2])  #prints 0 to 2 indexes but not print index 2 element , i.e end-1=end

print(newTuple[:2])  #prints 0 to 2 index but not print index
print(newTuple[2:])


#condition check
if "Sanjita" in newTuple:
    print("yes ,sanjita is in newTuple")