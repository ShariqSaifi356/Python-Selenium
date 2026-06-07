def is_harshad_number(num : int) -> bool:
    digit_sum  = 0
    tempNumber = num
    
    if num < 0:
        return False
    
    while tempNumber != 0:
        digit = tempNumber % 10
        digit_sum  = digit_sum  + digit
        tempNumber //= 10
        
    if digit_sum == 0:
        return False

    return num % digit_sum == 0

if __name__ == "__main__":
    
    number = 18
    print(f"{number} is a Harshad Number or not state True/False: {is_harshad_number(number)}")
    