# define the nth number from the fibonacci numbers
#fibonacci numbers: 1,1,2,3,5,8,13... (starts with two 1s and the number is the sum of two prev numbers)
from unittest import result


def fibonacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    
    return result
print(fibonacci(3)) #to find the 3rd number, answer is 2 

# using dynamic programming method
def fibonacci_2(n):
    result = 0
    memoi = [None] * (n+1)
    for i in range(len(memoi)-1):
        if memoi[n] != None:
            return memoi[n]

    else:
        if n ==1 or n ==2:
            result = 1
        else: 
            memoi[n] = fibonacci(n-2) + fibonacci(n-1)
            result = memoi[n]
    return result
print(fibonacci_2(5)) # to find the 5th number, answer is 5

#bottom-up approach
def fibonacci_3(n):
    result = 0
    if n ==1 or n ==2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
        
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        
    return bottom_up[n]    

print(fibonacci_3(10))


