last = int(input())

num = 1
sum = 0

while True:
    if sum >= last :
        break
    sum += num
    num += 1

print(sum)