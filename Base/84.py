a, b, c, d = map(int, input().split())
mega = a * b * c * d / 8 / 1024 / 1024

print(format(mega,".1f"),"MB")