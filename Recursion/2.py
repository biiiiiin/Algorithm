def recursion(num):
    if num == 1 :
        print(num)
        return ;
    else:
        print(num)
        recursion(num = num - 1)
        
inputNum = int(input())

recursion(inputNum)