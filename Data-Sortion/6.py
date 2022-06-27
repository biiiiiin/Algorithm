count = int(input())

arr = list(map(int, input().split()))

sortedArr = sorted(arr)

for i in range(count):
    print(sortedArr.index(arr[i]), end=" ")