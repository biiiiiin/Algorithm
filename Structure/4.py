from re import L
import re


count = int(input())

arr = []

for i in range(count):
    addArr = []
    name, score1, score2, score3 = input().split()
    
    addArr.append(name)
    addArr.append(int(score1))
    addArr.append(int(score2))
    addArr.append(int(score3))

    arr.append(addArr)
    
arr.sort(key=lambda x:x[1], reverse=True)

secondRank = 1
thirdRank = 1

for i in range(1, count):
    if arr[0][2] <arr[i][2]:
        secondRank += 1
    if arr[0][3] <arr[i][3]:
        thirdRank += 1

print(arr[0][0], secondRank, thirdRank)