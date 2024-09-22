Name=['Erika', 'Erish', 'Erina']
Sname=['Erika', 'Erish', 'Erina']
Newname=Name
print(Name is Newname)  #return true cuz Newname is the same object as Name

print(Sname is Newname) #return false cuz Name is not the same object as Sname, even if they have the same content



print(Name is not Newname)  #return false cuz Newname is the same object as Name

print(Sname is not Newname) #return True cuz Name is not the same object as Sname, even if they have the same content
