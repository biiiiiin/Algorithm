def superSum(k, n):
    sum = 0
    if k == 0:
        return n
    else:
        for i in range(n+1):
            sum += superSum(k-1, i)
    return sum

inputList = []

i = 0
while True:
    try:
        inputList.append([])
        k, n = map(int, input().split())
        
        inputList[i].append(k)
        inputList[i].append(n)
        i += 1
    except EOFError:
        break

    
for i in range(len(inputList)):
    print(superSum(inputList[i][0], inputList[i][1]))