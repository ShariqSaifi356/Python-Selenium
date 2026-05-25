import math as m

def is_disarium_number(num : int) -> bool:
    "This method will check the given number is a Disarium number or not."

    tempNum = num
    count = len(str(num))
    total = 0

    if num < 0:
        return False
    
    while tempNum != 0:
        digit = tempNum % 10
        total = total + int(m.pow(digit, count))
        count -= 1
        tempNum //= 10
    
    return total == num

if __name__ == "__main__":
    number = 135
    print(f"{number} is a Disarium number state True/False: {is_disarium_number(number)}")
