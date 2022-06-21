count = int(input())

list = list(map(int, input().split()))

for i in range(count-1, -1, -1) :
    print(list[i], end=" ")