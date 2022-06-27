count = int(input())

arr = []

for i in range(count):
    arr.append([])
    name, score = input().split()
    arr[i].append(name)
    arr[i].append(int(score))
    
arr.sort(key=lambda x:x[1], reverse=True)

print(arr[2][0])