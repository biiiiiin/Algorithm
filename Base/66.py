nums = []
a, b, c = map(int, input().split())

nums.append(a)
nums.append(b)
nums.append(c)

for i in nums :
    if i % 2 == 0 :
        print("even")
    else:
        print("odd")