temp = int(input())
result = (('A' if(temp < 0) else 'C') if(temp % 2 == 0) else ('B' if(temp < 0) else 'D'))
print(result)