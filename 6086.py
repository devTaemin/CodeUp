limit = int(input())
n = 1
total = 0
while(True):
    total += n
    if(total >= limit): break
    n += 1
print(total)