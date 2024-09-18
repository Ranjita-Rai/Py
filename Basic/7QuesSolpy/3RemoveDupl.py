# particular list bata duplicate hatauni
def remove_duplicate(number):
    result=[]
    for num in number:
        if num not in result:
            result.append(num)

    return result
number= [1,2,3,4,5,1,2,3,4,5,6,7,8,9,8,7,6]
print(remove_duplicate(number))