
def is_spy_number(num : int) -> bool:
    '''This method will check whether the number is a spy number or not.'''
    
    digits_sum = 0
    digits_product = 1
    
    if num < 0:
        return False
    
    if num == 0:
        return True
    
    while num != 0:
        digit = num % 10
        digits_sum = digits_sum + digit
        digits_product = digits_product * digit
        num //= 10
        
    return digits_sum == digits_product

if __name__ == "__main__":
    number = 22
    print(f"{number} is a Spy number state True/False: {is_spy_number(number)}")
        