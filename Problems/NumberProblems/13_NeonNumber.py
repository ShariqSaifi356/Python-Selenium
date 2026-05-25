
def is_neon_number(num : int) -> bool:
    
    square = num ** 2
    total = 0
    
    if num < 0:
        return False
    
    while square != 0:
        digit = square % 10
        total = total + digit
        square = square // 10
        
    return num == total

if __name__ == "__main__":
    number = 9
    print(f"{number} is a Neon number state True/False: {is_neon_number(number)}")
    