def maxIndex(arr):
    maxNum = max(arr)
    return arr.index(maxNum)

count = int(input())

numList = list(map(int,input().split()));

print(maxIndex(numList)+1)