def minNumber(arr):
    minNum = min(arr)
    return minNum

count = int(input())

numList = list(map(int,input().split()));

print(minNumber(numList))