def is_prime(num : int) -> bool:
    '''This method will check the given number is prime or not.'''
    
    if (num <= 1):
        return False
    
    for i in range(2, num):
        if (num % i == 0):
            return False
        
    return True       
    
        
if __name__ == "__main__":
    number = 7
    print(f"{number} is a prime number T/F: {is_prime(number)}")
    help(is_prime)