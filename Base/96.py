a = []

for i in range(19) :
    b = []
    b = list(map(int, input().split()))
    a.append(b)
    
count = int(input())

for k in range(count):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(19):
        if i != x :
            if a[i][y] == 1 :
                a[i][y] = 0
            else :
                a[i][y] = 1
                
    for i in range(19):
        if i != y :
            if a[x][i] == 1 :
                a[x][i] = 0
            else :
                a[x][i] = 1
                
for i in range(19):
    for j in range(19):
        print(a[i][j], end=" ")
    print("")