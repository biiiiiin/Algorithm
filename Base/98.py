arr = []
antX = 1
antY = 1

for i in range(10):
    b = []
    b = list(map(int, input().split()))
    arr.append(b)
    
while antX != 9 and antY != 9 :
        
    if arr[antY][antX] == 2:
        arr[antY][antX] = 9
        break
    
    else:
        if arr[antY][antX] == 0:
            arr[antY][antX] = 9
            
        if arr[antY][antX+1] == 0 or arr[antY][antX+1] == 2:
            antX += 1
        else :
            antY += 1
            
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=" ")
    print("")