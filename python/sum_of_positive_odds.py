print('Enter a number: ')
n = int(input())
sum = 0
for i in range (n):
    if i < 0:
        sum += 0
    else:
        if i % 2 == 1:
            sum += i
        else:
            sum += 0
    
print(sum)