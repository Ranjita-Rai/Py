# comprehensive and dictionery
# yeuta list bata even num matra linxa and return in dictionery format ma sq. of that even num

def square_numbers(numbers):
    return {num:num**2 for num in numbers if num%2==0}
numbers=[1,2,3,4,5,6,7,8,9,10]
print(square_numbers(numbers))