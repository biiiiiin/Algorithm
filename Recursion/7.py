import sys
sys.setrecursionlimit(10**7)

def fivo(num, first, second):
    if num == 0:
        return first + second
    else:
        return fivo(num - 1, second, first + second)


input_num = int(input())

if input_num == 1 or input_num == 2:
    print(1)
else:
    print(fivo(input_num-3, first=1, second=1)%10009)