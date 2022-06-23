height, width = map(int, input().split())

arr = []

for i in range(height):
    arr.append([])
    for j in range(width):
        arr[i].append(0)
        
count = int(input())

for i in range(count) :
    length, dir, y, x = map(int, input().split())
    x -= 1
    y -= 1
    
    if dir == 1 :
        for j in range(length):
            arr[y+j][x] = 1
    else :
        for j in range(length):
            arr[y][x+j] = 1

for i in range(height): 
    for j in range(width):
        print(arr[i][j], end=" ")
    print("")