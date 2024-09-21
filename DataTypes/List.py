
List=[ "Ranjita", "Sanjita", "Kriti", "Samana"]
#List[1:2]=["Erika"]  #1:2 means that starting with 1 index(included) and end 2 index(excluded)
#print(List)   #replace sanjita 


#List [-1]=("kamana") #insert kamana to index -1 i.e last index with replacing the last element
#print(List) 


#List.insert(3, "Rojeena") #insert rojeena at 3 index, but not replacing already exist element just right shifting 
#print(List) 


if "Kriti" in List:
    print("Yes, Kriti is in list.")
else:
    print("NO, kriti isnot in list.")

for i in range (len(List)):
    print(List[i]) #print all