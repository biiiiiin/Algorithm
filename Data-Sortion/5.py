#Insertion Sortion
count = int(input())

arr = []

for i in range(count):
    arr.append(int(input()))
    
for i in range(1, count):
    key = arr[i]
    for j in range(i-1, 0, -1):
        if arr[j] > key:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        else:
            break
    
for i in range(count):
    print(arr[i])