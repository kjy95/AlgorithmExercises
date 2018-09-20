#bfs breadth first search : 너비우선 탐색
#세개의 경우가 계속 나오고 거기서 K가 되는 X값을 구해야함.
#LIST를 이용해야함.

N = int(input())
X = N
XLIST = list()
K = int(input())
#
XLIST.append({"cnt":0,"loc":X})
visited = 100001 * [False]
while len(XLIST) != 0:
    tempdic = XLIST.pop(0)
    cnt = tempdic['cnt']
    loc = tempdic["loc"]
    if loc<0 or loc>100000:
        continue
    if visited[loc]:
        continue
    visited[loc] = True
    
    if K==loc:
        print(cnt)
        break

    XLIST.append({"cnt":cnt+1,"loc":loc*2})    
    XLIST.append({"cnt":cnt+1,"loc":loc+1})
    XLIST.append({"cnt":cnt+1,"loc":loc-1})
    



"""depth = 1
count = 0
if N < K:
    if X*2<=100000 and X*2>=0 :
            XLIST.append(X*2)
        if X-1<=100000 and X-1>=0: 
            XLIST.append(X-1)
        if X+1<100000 and X+1>=0:
            XLIST.append(X+1)
    while X != K:
        X = XLIST.pop(0)
        if X*2<=100000 and X*2>=0 :
            XLIST.append(X*2)
        if X-1<=100000 and X-1>=0: 
            XLIST.append(X-1)
        if X+1<100000 and X+1>=0:
            XLIST.append(X+1)
        count+=1
        if count == pow(3, depth):
            depth+=1
    print(depth)

else:
    print(N-K)"""