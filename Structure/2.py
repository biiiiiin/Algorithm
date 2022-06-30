from re import L


count = int(input())

numList = list(map(int, input().split()))

arr = [0 for i in range(500000)]

for i in range(count):
    arr[numList[i]] += 1
    
for i in range(count):
    count = 0
    for j in range(numList[i]):
        if arr[j] > 0:
            count += 1
    print(count, end=" ")