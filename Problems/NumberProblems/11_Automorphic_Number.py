import math as m

def is_automorphic_number(num : int) -> bool:
    '''This method will check that the given number is an automorphic number or not.
    An automorphic number is an integer whose square ends in the exact same digits as the original number. For example, (25)^2 = 625, which ends in 25.
    '''
    
    count = 0
    tempNum = num
    
    if num < 0:
        return -1
    
    while tempNum != 0:
        count += 1
        tempNum //= 10
    
    square = int(m.pow(num, 2))
    lastDigits = square % int(m.pow(10, count))
    
    return lastDigits == num

if __name__ == "__main__":
    number = 376
    print(f"{number} is an automorphir number state True or False: {is_automorphic_number(number)}")  
