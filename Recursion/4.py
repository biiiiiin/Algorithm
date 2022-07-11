def add(num):
    if num == 0 :
        return 0;
    else:
        return add(num - 1) + num
    
print(add(int(input())))