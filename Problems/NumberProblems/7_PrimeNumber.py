def is_prime_1(num : int) -> bool:
    '''1. This method will check the given number is prime or not.'''
    
    if (num <= 1):
        return False
    
    for i in range(2, num):
        if (num % i == 0):
            return False
        
    return True    


def is_prime_2(num : int) -> bool:
       '''2. This method will check the given number is prime or not.'''
       
       c = 2
       if (num <= 1):
           return False
       
       while (c * c <= num):
           if (num % c == 0):
               return False
           c = c + 1
           
       return True
               
       
    
        
if __name__ == "__main__":
    number = 37
    print(f"{number} is a prime number T/F: {is_prime_1(number)}")
    help(is_prime_1)
    print(f"{number} is a prime number T/F: {is_prime_2(number)}")
    help(is_prime_2)