# def findMax(num1, num2):
#     i = 2
#     maxDiv = 1
#     while i != num1 and i != num2:
#         if num1 % i == 0 and num2 % i == 0 :
#             num1 //= i
#             num2 //= i
#             maxDiv *= i
#             i = 2
#         else:
#             i += 1
            
#     return maxDiv


# def findMax(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return findMax(num2, num1%num2)


import math

num1, num2 = map(int, input().split())

# commonMax = findMax(num1, num2)
commonMax = math.lcm(num1, num2)

# print(int(num1*num2/commonMax))
print(commonMax)