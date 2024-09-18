def count_occurance(numbers):
    count={}
    for num in numbers:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    return count

numbers=[1,2,3,4,1,2,3,4,5,6,7,6,5,6,3,4,3,2,1]
result=count_occurance(numbers)
print(result)

# yp prg ma list ma numbers kati choti repeat xa vanera count gareko and output chai  dictionary ma 