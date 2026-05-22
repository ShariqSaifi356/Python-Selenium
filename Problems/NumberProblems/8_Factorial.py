
def factorial(num : int) -> int:
    
    fact = 1
    
    if num < 0:
        return ValueError("Factorial is not defined for negative numbers")
    
    for i in range(2, num + 1):
        fact = fact * i
        
    return fact

if __name__ == "__main__":

    num = 0
    print(f"The factorial of {num} is : {factorial(num)}")        