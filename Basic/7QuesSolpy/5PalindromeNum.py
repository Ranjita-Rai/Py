def IS_Palindrome_num(num):
    num_str=str(num)
    left=0
    right=len(num_str)-1   #compare garda string ko legth -1 chai hamro index sanga eqal hunxa eg: ranjita ko length 7 xa ani last ko index chai 6 xa , tei vayera 7-1=6
    # name="ranjita"
    while left<right:
        if num_str[left]!=num_str[right]:
            return False
        left +=1
        right -=1

    return True

test_numbers=[ 'ranj', 45654, 34545 ] #string ni milni rahexa
for number in test_numbers:
    if IS_Palindrome_num(number):
        print(f"{number} is a palindrome.")
    else:
         print(f"{number} is not a palindrome.")