callCnt = int(input())

calls = list(map(int, input().split()))

count = []

for i in range(23):
    count.append(0)
    
for i in range(len(calls)):
    count[calls[i]-1] += 1
    
for i in range(23):
    print(count[i], end=" ")