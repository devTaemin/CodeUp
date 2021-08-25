value = input()
n = 0
if(value=='A'):
    n = 10
elif(value=='B'):
    n = 11
elif(value=='C'):
    n = 12
elif(value=='D'):
    n = 13
elif(value=='E'):
    n = 14
elif(value=='F'):
    n = 15

for i in range(1,16):
    print('%X' % n, '*%X' % i, '=%X' % (n*i), sep='')
