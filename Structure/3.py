count, rank = map(int, input().split())

arr = []

for i in range(count):
    addArr = []
    name, score = input().split()
    
    addArr.append(name)
    addArr.append(int(score))
    
    arr.append(addArr)
    
arr.sort(key=lambda x:x[1], reverse=True)

for i in range(rank):
    print(arr[i][0])