from re import L


binaryNumber = []

def binaryNum(num):
    if num == 0:
        return;
    else:
        if num % 2 == 0:
            binaryNumber.append(0)
        else:
            binaryNumber.append(1)
    binaryNum(num//2)

input_num = int(input())

if input_num == 0 :
    print(0)
else:
    binaryNum(input_num)
    binaryNumber.reverse()
    answer = "".join(map(str,binaryNumber))
    print(answer)