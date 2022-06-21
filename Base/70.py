# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

num = int(input())

if num // 3 == 1 :
    print("spring")
elif num // 3 == 2:
    print("summer")
elif num // 3 == 3:
    print("fall")
else :
    print("winter")