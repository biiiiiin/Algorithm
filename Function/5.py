def addFun(lastNum):
    sum = 0
    for i in range(lastNum+1):
        sum += i
    return sum

lastNum = int(input())

print(addFun(lastNum))