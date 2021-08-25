limit = int(input())
total = 0
i = 1
while(True):
    total += i
    if(total >= limit):
        break
    i += 1

print(i)