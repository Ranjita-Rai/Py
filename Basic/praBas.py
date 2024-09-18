# print("Hello World !")


# if 1>2:
#     print("one is greater than 2")
# else:
#     print(" two is greater than one")


# a=100
# b="hello world"
# print (a)
# print (b)


# x=int(5)  #int type variable
# y=float(7)   #floating type variable
# z=y          # assigning value of y in z
# print(z)


# x="3"
# y="5"
# print(x+y) #string concatinate
# x=5
# y=10
# print(x+y)   #Sum operation


# x=10
# y="ranjita"
# print(type(x))   #type check
# print(type(y))


# a="asmita"
# b='asmita'
# print(a)
# print(b)    #doesn't matter single or double quotation


# a=5
# A="ranjita"    # a and A are different, variable name are case sensative
# print(a)
# print(A)


# assign multiple values:
# x,y="ranjita",'rai'
# print (x)
# print(y)
# a=b="Ranjita"
# print(a)
# print(b)
# fruits=["Apple", "Orange", "Grapes"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)


# x="python is awesome"
# print(x)

# x="python "
# y="is "
# z="awesome"
# print(x,y,z)   #String concatination 
# print(x+y+z)


# x=10
# y="python"
# print(x,y)  #if we use print(x+y), python will give youu an error


# Scope of variable
# x="awesome"
# def myfun():
#     x="fantastic"
#     print("python is "+x)
# myfun()
# print("python is "+x)

#using global variable
# x="awesome"
# def myfun():
#     global x
#     x="fantastic"
#     print("python is "+x)
# myfun()
# print("python is "+x)


##Variable Type
# x=1   #int
# y=1.5   #float
# z=2j    #complex
# print(x)
# print(y)
# print(z)


# a, b = 1, "2"
# c = int(b)  #type casting
# sum = a + c
# print(sum)


##WAP to print area of square
# a=10
# area=a*a
# print(area)

# #WAP to input two floating num abd print their average
# a=10.3
# b=9.7
# average=(a+b)/2
# print(average)


# Wap to input 2 num and print true if a >=b ,otherwise false
# a=10
# b=20
# if a>=b :
#     print("true")
# else:
#     print("false")


# b="hello, world"
# print(b[3:12]) #print to the 3rd index up to its length(12)


#lower and upper string
# x="Ranjita"
# print(x.upper())
# print(x.lower())


#strip() rempoves the whitespaces from the beginning or the end
# a="   Ranjita   "
# print(a.strip())


# replace()
# a="Hello BCA"
# print(a.replace("C","B"))     #replace C by B, Output: BBA


# split()
# a="Hello, world"
# print(a.split(",")) 


#String concatination
# a="hello"
# b="python"  
# c=a + " "+b              #And the " " is for space between a and b
# print(c)


#String formatting
# price=150
# text=f"the price of laptop is {price}k"
# print(text)
# text=f"The price of laptop is {price:.2f}k"
# print(text)
# text=f"The price of laptop is {15000*100}"
# print(text)


#use of escape
# text="hello bca \"4th\" Semester"
# print(text)



name='python'
if name=='java' or 'c++' or 'js':
    print("login sucessful")
else:
    print("not valid")