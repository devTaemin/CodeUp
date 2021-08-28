height, width = map(int, input().split())
arr_2D = [[0 for i in range(width)] for j in range(height)]
num = int(input())

for _ in range(num):
    l, d, x, y = map(int, input().split())
    x -= 1  #실제로 들어가는 x좌표 (height)
    y -= 1  #실제로 들어가는 y좌표 (width)

    if(d == 0):
        for col in range(l):
            if(y+col < width):
                if(arr_2D[x][y+col] == 0):
                    arr_2D[x][y+col] = 1
                else:
                    arr_2D[x][y+col] = 0
    else:
        for row in range(l):
            if(x+row < height):
                if(arr_2D[x+row][y] == 0):
                    arr_2D[x+row][y] = 1
                else:
                    arr_2D[x+row][y] = 0


for i in range(height):
    for j in range(width):
        print(arr_2D[i][j], end=' ')
    print()