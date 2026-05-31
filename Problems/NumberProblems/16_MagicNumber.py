
def check_one(num : int) -> int:
    
    if num <= 0 : return -1
    
    sum = 0
    
    while num > 0 or sum > 9:
        
        if num == 0:
            num = sum
            sum = 0
            
        digit = num % 10
        sum = sum + digit
        num = num // 10
        
    return sum

if __name__ == "__main__":
    number = 12345
    if check_one(number) == 1:
        print(f"{number} is a Magic number")
    else: 
        print(f"{number} is not a Magic number")