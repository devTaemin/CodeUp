w, h, b = input().split()
result = format((int(w) * int(h) * int(b) / 8 / 1024 / 1024), '.2f')
print(result, "MB")
