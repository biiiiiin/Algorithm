a, b, c = map(int, input().split())

if a > b:
    min = b
else :
    min = a
    
if min > c :
    print(c)
else :
    print(min)