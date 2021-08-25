n = int(input())
students = [0 for i in range(23)] #0(1) ~ 22(23)
d = input().split()

for i in d:
    index = int(i) - 1
    students[index] += 1

for i in students:
    print(i, end=' ')