# 헤르츠(h) * 비트(b) * 채널(c) * 녹음시간(s)
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
result = format((h * b * c * s / 8 / 1024 / 1024), '.1f')
print(result, "MB")