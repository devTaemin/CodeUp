a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
start = max(a,b,c)

while(True):
    if(start % a == 0 and start % b == 0 and start % c == 0):
        print(start)
        break
    start += 1

