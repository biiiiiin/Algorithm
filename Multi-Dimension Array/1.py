arr = []
num = int(input())

for i in range(num):
    arr.append([])
    for j in range(num):
        arr[i].append(num * i + j + 1)
        print(arr[i][j], end=" ")
    print()