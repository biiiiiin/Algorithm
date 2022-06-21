count = int(input())

a = []

for i in range(20) :
    a.append([])
    for j in range(20):
        a[i].append(0);
        

for i in range(count):
    x, y = map(int, input().split())
    a[x][y] = 1
    
for i in range(1, 20):
    for j in range(1, 20):
        print(a[i][j], end=" ")
    print("")