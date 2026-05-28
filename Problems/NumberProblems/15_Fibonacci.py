def fibonacci(num : int) -> int:
    
    if num < 0:
        return -1
    
    elif num == 0:
        return 0
    
    elif num == 1 or num == 2:
        return 1
    
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
    
# Function to print Fibonacci series
def fibo_series(num: int):

    # First number
    a = 0

    # Second number
    b = 1

    # Loop to print Fibonacci series
    for _ in range(num+1):

        # Print current number
        print(a, end=" ")

        # Calculate next Fibonacci number
        c = a + b

        # Update values
        a = b
        b = c
    
    
if __name__ == "__main__":
    number = 9
    print(fibo_series(number))