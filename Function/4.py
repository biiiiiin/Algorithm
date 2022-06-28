def findIndex(numList, findNum):
    for i in range(len(numList)):
        if numList[i] == findNum:
            return i+1
    return -1

count = int(input())

numList = list(map(int, input().split()))

findNum = int(input())

print(findIndex(numList, findNum))