c = input()

c = c.lower()

oneC = 0
twoC = 0

for i in range(len(c)):
    if c[i] == "c":
        oneC += 1
    if i != len(c)-1:
        if c[i] == "c" and c[i+1] == "c" :
            twoC += 1

print(oneC)
print(twoC)