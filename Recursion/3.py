def oddBetween(start, end):
    if start % 2 != 0:
        print(start, end=" ")
    
    if start == end:
        return ;
    
    oddBetween(start+1, end)
    

start, end = map(int, input().split())

oddBetween(start, end)