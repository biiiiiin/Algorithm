a = input()

open = 0
close = 0

for i in range(len(a)):
    if a[i] == "(" :
        open += 1
    elif a[i] == ")" :
        close += 1
        
print(open, close)