arr = []

for i in range(19):
    arr.append([])
    for j in range(19):
        arr[i].append(0)
        
count = int(input())
for i in range(count):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    arr[y][x] = 1

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=" ")
    print()