def reverseNumber(num):
    originalNumber = num
    reversedNum = 0
    while(num != 0):
        lastNum = num % 10
        reversedNum = (reversedNum * 10) + lastNum
        num = num // 10
        
    if(originalNumber == reversedNum):
        print(f"{originalNumber} number is a palindrome.")
    else:
        print(f"{originalNumber} number is not a palindrome.")
        
if __name__ == "__main__":
     reverseNumber(121)