def swap_1(a, b):
    print("Before swap: ", a, " ", b)
    a = a + b
    b = a - b
    a = a - b
    print("After swap: ", a, " ", b)

def swap_2(a, b):
    # Python style
    print("Before swap: ", a, " ", b)
    a, b = b, a
    print("After swap: ", a, " ", b)
    
        
if __name__ == "__main__":
    swap_1(10, 20)
    swap_2(22, 11)
    
