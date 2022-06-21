last = int(input())
num = 1

while True:
    if last * 2 <= num * (num + 1) :
        print(num)
        break
    num += 1