n = int(input())
arr = input().split()
target = int(arr[0])
for i in range(1, n):
    if(target > int(arr[i])):
        target = int(arr[i])

print(target)