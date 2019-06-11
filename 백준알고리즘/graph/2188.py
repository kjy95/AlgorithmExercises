import sys

N ,M= (sys.stdin.readline().split())
N = int(N)
M = int(M)
hopenum = []
hopelist = []
homelist = [0] * (M-1)
def findMin(hopenum):
    tempindex = hopenum.index(min(hopenum))
    hopenum[tempindex] = 201
    return tempindex
for _ in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    hopenum.append(int(array[0]))
    del array[0]
    hopelist.append(array)

for _ in range(N):
    tempindex = findMin(hopenum)
    for temphopelist in hopelist[tempindex]:
        if homelist[int(temphopelist) ] ==0:
            homelist[int(temphopelist)] = 1
            break
        else:
            continue
            
sys.stdout.write(str(homelist.count(1)))