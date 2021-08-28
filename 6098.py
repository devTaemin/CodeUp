# 오른쪽으로 움직이다가 벽인 경우는 아래로 움직인다
# 오른쪽에 길이 있으면 다시 오른쪽으로 이동한다
# 즉 먹이를 찾거나 움직일 수 없을 때 까지 오른쪽 혹은 아래로 이동한다
# 0이 갈 수 있는 곳, 1이 벽 또는 장애물, 2가 먹이 위치, 맨 아래 가장 오른쪽 위치 종점, 이동 경로는 9로 표시

map = [list(map(int, input().split())) for _ in range(10)]
x = 1
y = 1
stop = False

while(not stop):
    # Marking
    if(x == 8 and y == 8):
        map[x][y] = 9
        stop = True

    if(map[x][y] == 0):
        map[x][y] = 9

    if(map[x][y] == 2):
        map[x][y] = 9
        stop = True

    # Move
    if(map[x][y+1] == 0):
        # 우측 이동이 가능한 경우
        y += 1
    elif(map[x][y+1] == 2):
        y += 1
    else:
        # 우측 이동이 불가능한 경우
        if(map[x+1][y] == 0):
            x += 1
        elif(map[x+1][y] == 2):
            x += 1
        else:
            stop = True

for row in range(10):
    for col in range(10):
        print(map[row][col], end=' ')
    print()