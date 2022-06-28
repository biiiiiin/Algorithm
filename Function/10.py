def findIndex(numList, maxNum):
    if maxNum > numList[-1]:
        return len(numList)+1
    else:
        for i in range(len(numList)):
            if maxNum <= numList[i]:
                return i+1

count = int(input())

numList = list(map(int, input().split()))

maxNum = int(input())

print(findIndex(numList, maxNum))