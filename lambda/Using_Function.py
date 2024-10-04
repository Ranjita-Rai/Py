def fun(n):
    return lambda a: a*a*n+1
    
myfunction=fun(5)
print(myfunction(7))


'''
def func():
    a=int(input("enter a number: "))
    b=int(input("enter 2nd number: "))
    d=a+b
    return lambda c: d  
print(func())  '''