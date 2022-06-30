count = int(input())

arr = []

for i in range(count):
    addArr = []
    index, gas = map(int, input().split())
    addArr.append(index)
    addArr.append(gas)
    
    arr.append(addArr)
    
arr.sort(key=lambda x:x[0])

for i in range(count):
    print(arr[i][0], arr[i][1])