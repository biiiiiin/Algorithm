def drawStar(num):
    if num == 0:
        return ;
    else:
        print("*", end="")
        return drawStar(num-1)

def star(start, end):
    if start == end+1:
        return;
    else:
        drawStar(start)
        print()
        return star(start+1,end)
    
end = int(input())

star(1, end)