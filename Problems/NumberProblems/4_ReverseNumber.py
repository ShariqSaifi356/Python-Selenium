def reverseNumber(num):
    
    reversedNum = 0
    while(num != 0):
        lastNum = num % 10
        reversedNum = (reversedNum * 10) + lastNum
        num = num // 10
        
    print(f"The reversed number is {reversedNum}")
        
if __name__ == "__main__":
     reverseNumber(12345)