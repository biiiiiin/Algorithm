arr = []
num = int(input())

for i in range(num):
    arr.append([])
    for j in range(num):
        arr[i].append(num * i + j + 1)

for i in range(num):
    for j in range(num):
        print(arr[i][num-1-j], end=" ")
    print()