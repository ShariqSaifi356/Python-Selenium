import math as m

def armstrong_number(num : int) -> int:
    total = 0
    count = 0
    tempNumber = num
    
    if num < 0:
        return -1
    
    while tempNumber != 0:
        count = count + 1
        tempNumber //= 10
        
    while num != 0:
        digit = num % 10
        total = total + int(m.pow(digit, count)) # m.pow returns float so type casting it.
        num //= 10
        
    return total

if __name__ == "__main__":
    number = 0
    
    if number == armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")