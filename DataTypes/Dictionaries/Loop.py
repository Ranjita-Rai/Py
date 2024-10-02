mydict={
    "Name": "Ranjita",
    "Age": 18,
    "Height": 5.2,
    "Address":'kalanki'
}
for i in mydict:
     #Output:  Name, Age Height Address
    print(i)

for i in mydict:
     #output: Ranjita, 18, 5.2, kalanki
    print(mydict[i])


#using values() method
for i in mydict.values():
    #output: Ranjita, 18, 5.2, kalanki
    print(i) 


#uding keys() method
for i in mydict.keys():  
    #Output:  Name, Age Height Address
    print(i)


#using items() method
for i,j in mydict.items():
    print(i,j) 
    '''output: Name Ranjita
    Age 18
    Height 5.2
    Address kalanki'''