words = []

suc = True

for i in range(3):
    word = input()
    words.append(word)
    
if words[0][-1] != words[1][0]:
    suc = False
elif words[1][-1] != words[2][0]:
    suc = False
elif words[0][0] != words[2][-1]:
    suc = False

if suc:
    print("good")
else :
    print("bad")