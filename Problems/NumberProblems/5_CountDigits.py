def countDigits(num):    
    count = 0
    while(num != 0):
        count += 1
        num = num // 10
        
    print(f"The count is {count}")
        
if __name__ == "__main__":
     countDigits(12345)