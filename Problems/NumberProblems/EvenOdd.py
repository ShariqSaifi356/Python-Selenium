def evenOdd(num):
    
    if (num <= 0):
        print(f"{num} is neither even nor odd.")
    elif (num % 2 == 0):
        print(f"{num} is a even number.")
    else:
        print(f"{num} is a odd number.")
        
if __name__ == "__main__":
    evenOdd(2)
    
