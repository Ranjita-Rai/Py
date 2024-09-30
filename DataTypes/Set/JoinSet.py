
myNum={23,41,45,23,12,56,77,54,22}
myStr={"Hello","World","Python","Programming","Language"}
#using union()

result=myNum.union(myStr)
print(result)

#join tuple and set using union()
NumTuple=(23,41,45,23,12,56,77,54,22)
StringSet={"Hello", "Python", "Programmer"}
result=StringSet.union(NumTuple)
print(result)

#using '|' operator instead of union
result=myNum | myStr
print(result)

###using update()
result=myNum.update(myStr)
print(result)



####Using Intersection()####
string={"hello", "Ranjita"}
string2={"hello", "python"}
result=string.intersection(string2)
print(result)

#using intersection_update()
result=string.intersection_update(string2)
print(result)

#using '&' operator instead of intersection
result=string & string2
print(result)


#####Using Difference()####
string={"hello", "World"}
string2={"hello","bca","students"}
result=string.difference(string2)
print(result)

#using difference_update()
result=string.difference_update(string2)
print(result)

#using "-" operator
result=string - string2
print(result)

#using '^' operator
result=string ^ string2
print(result)
#power ("^") and symmetric difference are same
#using symmetric_difference()
result=string.symmetric_difference(string2)
print(result)

#usingsymmetric_differsnce_update()
result=string.symmetric_difference_update(string2)
print(result)