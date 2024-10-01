NewDict={
    "Name":"Ranjita",
    "Age":18,
    "Gender":"Female"
}
print(NewDict)

 #using get()
result= NewDict.get("Name")
print(result) #output:Ranjita

#using keys()
result=NewDict.keys()
print (result)  #output: dict_keys(['Name', 'Age', 'Gender'])

#using values()
result=NewDict.values()
print(result) #output: dict_values(['Ranjita', 18, 'Female'])

#using items()
result=NewDict.items()
print(result) #output:  dict_items([('Name', 'Ranjita'), ('Age', 18), ('Gender', 'Female')])


#condition
if "Age" in NewDict:
    print("yes it is.")
else:
    print("not found !!")