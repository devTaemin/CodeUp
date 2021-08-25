end = int(input())
n = 1
total = 0
while(n <= end):
    if(n % 2 == 0):
        total += n
    n += 1
print(total)