start, mul, add, count = map(int, input().split())

for i in range(count-1):
    start = start * mul + add

print(start)