def greatestNumberUsingInbuiltFunction(num1, num2, num3):
    print(f"The max num is: {max(num1, num2, num3)}") 
    
    
def greatestNumber(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        print(f"The max num is: {num1}")
        
    elif(num2 > num1 and num2 > num3):
        print(f"The max num is: {num2}") 
    
    else:
        print(f"The max num is: {num3}") 
        
        
if __name__ == "__main__":
    greatestNumber(45, 12, 89)
    greatestNumberUsingInbuiltFunction(800, 1000, 45)
    
