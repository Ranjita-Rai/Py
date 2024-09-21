List=[ "Ranjita", "Sanjita", "Kriti", "Samana"]
'''
NewList=[]
for i in List:
    if "n" in i:        ##Print only those elements that have the letter n
      NewList.append(i)

print(NewList)
'''


'''
NewList=[i for i in List if "n" in i]  ##just in onelineeee
print(NewList)
'''


'''
newlist=[i if i!="Ranjita" else "Sangita" for i in List]  ##Return sangita (replace ranjita by sangita)
print(newlist)
'''