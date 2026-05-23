
def sum_of_digits(num : int) -> int:
    '''This method will return the sum of digits of a number.'''
    
    total = 0
    
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
    
    while num != 0:
        digits = num % 10
        total = total + digits
        num = num // 10
        
    return total

if __name__ == "__main__":
    number = 1234
    print(f"The sum of digits of number {number} is: {sum_of_digits(number)}")