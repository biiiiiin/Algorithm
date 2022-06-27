#Selection Sortion
count = int(input())

arr = []

for i in range(count):
    arr.append(int(input()))
    
for i in range(count-1):
    least = i
    for j in range(i, count):
        if arr[j] < arr[least]:
            least = j
    arr[i], arr[least] = arr[least], arr[i]
    
for i in range(count):
    print(arr[i])