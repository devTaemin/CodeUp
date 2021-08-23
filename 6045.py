a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a + b + c
avg = format(float(sum / 3), '.2f')
print(sum, avg)