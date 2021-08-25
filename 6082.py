limit = int(input())
for i in range(1, limit+1):
    first = i // 10
    second = i % 10

    if(i < 10):
        if(second % 3 == 0):
            print('X', end=' ')
        else:
            print(i, end=' ')
    else:
        if(i % 10 == 0):
            #10으로 나누어 떨어지는 수
            if(first % 3 == 0):
                print('X', end=' ')
            else:
                print(i, end=' ')
        else:
            if(first % 3 == 0 or second % 3 == 0):
                print('X', end=' ')
            else:
                print(i, end=' ')