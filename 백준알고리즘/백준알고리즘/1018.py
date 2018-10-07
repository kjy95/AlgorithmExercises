import sys
m,n = map(int, sys.stdin.readline().split())
chasestr = list()
doubleListB = [[0]*m for i in range(n)]
doubleListW = [[0]*m for i in range(n)]

for _ in range(n):
    chasestr.append(sys.stdin.readline().rstrip())
i = 0
for temp in chasestr:
    posW = [pos for pos, char in enumerate(temp) if char =="W"]
    posB = [pos for pos, char in enumerate(temp) if char =="B"]
    
    if i%2==0:
        if posW[i] == i:
            doubleListW[i] = 0
            doubleListB[i] = 0
        else:
            doubleListW[i] = 1
            doubleListB[i] = 0
    else:
        if posW[i] == i:
            doubleListW[i] = 0
            doubleListB[i] = 0
        else:
            doubleListW[i] = 1
            doubleListB[i] = 0

    i +=1
    print(doubleListB)
    print(doubleListW)