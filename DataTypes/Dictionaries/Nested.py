newDict={
    "child1":{
        "Name": "Erika",
        "Address":"Kalanki",
        "Age":10

    },
    "child2":{
        "Name": "Ishika",
        "Address":"Kalimati",
        "Age":8

    },
    "child3":{
        "Name": "Erish",
        "Address":"Lagankhel",
        "Age":3
    }

}
print(newDict)
print(newDict["child1"]["Address"])

for x, obj in newDict.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

