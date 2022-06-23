arr = []

y, x = map(int, input().split())

inputNum = x * y

for i in range(y):
    arr.append([])
    list = []
    for j in range(x):
        list.append(inputNum)
        print(inputNum, end=" ")
        inputNum -= 1
    arr[i].append(list)
    print()