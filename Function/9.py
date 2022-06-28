def maxi(numList, start, end):
    arr = []
    if start == end:
        return numList[start-1]
    else :
        for i in range(start-1, end):
            arr.append(numList[i])
        return max(arr)

count = int(input())

numList = list(map(int, input().split()))

start, end = map(int, input().split())

print(numList.index(maxi(numList, start, end))+1)