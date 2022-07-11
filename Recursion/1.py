def recursion(startNum, num):
    if startNum == num :
        print(startNum)
        return;
    else :
        print(startNum)
        recursion(startNum+1, num)

input_num = int(input())

recursion(1,input_num)