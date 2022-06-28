def reverseNum(num):
    while num != 0 :
        print(num % 10, end="")
        num //= 10

num = int(input())

reverseNum(num)