r, g, b = input().split()
count = 0
for i in range(0, int(r)):
    for j in range(0, int(g)):
        for k in range(0, int(b)):
            count += 1
            print(i, j, k)
print(count)