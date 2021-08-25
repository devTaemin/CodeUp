arr_2D = [[0 for i in range(20)] for j in range(20)]
num = int(input())
for i in range(num):
    row, col = input().split()
    row = int(row)
    col = int(col)
    arr_2D[row-1][col-1] = 1

for i in range(19):
    for j in range(19):
        print(arr_2D[i][j], end = ' ')
    print()


