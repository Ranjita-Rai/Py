List=[ "Ranjita", "Sanjita", "Kriti", "Samana"]
#using slice(:) operator

List[1:2]=["Erika"]  #1:2 means that starting with 1 index(included) and end in 2 index(excluded,means that end-1=end )
print(List)   #replace sanjita 




List [-1]=("kamana") #insert kamana to index -1 i.e last index with replacing the last element
print(List) 



#using insert() 
List.insert(3, "Rojeena") #insert rojeena at 3 index, but not replacing already exist element just right shifting 
print(List) 


