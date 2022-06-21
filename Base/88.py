start, diff, count = map(int, input().split())

for i in range(count-1):
    start += diff

print(start)