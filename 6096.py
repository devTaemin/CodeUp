arr_2D = [list(map(int, input().split())) for i in range(19)]

n = int(input())
for i in range(n):
    row, col = input().split()
    row = int(row) - 1
    col = int(col) - 1
    for i in range(0,19):
        if(i != row):
            if(arr_2D[i][col] == 1):
                arr_2D[i][col] = 0
            else:
                arr_2D[i][col] = 1
    for j in range(0,19):
        if(j != col):
            if(arr_2D[row][j] == 1):
                arr_2D[row][j] = 0
            else:
                arr_2D[row][j] = 1

for i in range(19):
    for j in range(19):
        print(arr_2D[i][j], end=' ')
    print()