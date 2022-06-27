#Bubble Sortion
count = int(input())

arr = []
for i in range(count):
    arr.append(int(input()))
    
# for i in range(count-1):
#     for j in range(i, count-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
arr.sort()
            
for i in range(count):
    print(arr[i])