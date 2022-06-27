arr = []

num1, num2, num3 = map(int, input().split())

arr.append(num1)
arr.append(num2)
arr.append(num3)

for i in range(3):
    least = min(arr)
    print(least, end=" ")
    arr.remove(least)