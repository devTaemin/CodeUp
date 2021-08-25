n = int(input())
arr = input().split()

for i in range(0, n):
    index = n - i - 1
    print(arr[index], end=' ')