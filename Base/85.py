a, b, c = map(int, input().split())
mega = a * b * c  / 8 / 1024 / 1024

print(format(mega,".2f"),"MB")