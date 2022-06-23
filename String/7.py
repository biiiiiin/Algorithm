password = input()

for i in range(len(password)):
    word = ord(password[i])
    print(chr(word+2), end="")
print()

for i in range(len(password)):
    word = ord(password[i])
    print(chr((word*7)%80+48), end="")