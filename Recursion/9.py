collatz_list = []

def collatz(num):
    if num == 1:
        return ;
    else:
        if num % 2 == 1:
            collatz_list.append(num * 3 + 1)
            return collatz(num * 3 + 1)
        else:
            collatz_list.append(num // 2)
            return collatz(num // 2)
        
input_num = int(input())

collatz_list.append(input_num)

collatz(input_num)

collatz_list.reverse()

print(*collatz_list, sep="\n")