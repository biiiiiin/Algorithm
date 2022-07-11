import sys
sys.setrecursionlimit(10**7)

def fect(num):
    if num == 1:
        return 1
    else:
        return fect(num - 1) * num
    
print(fect(int(input())))