import sys
level = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
result = list()
for _ in range(level):
    tempnode = list()

    for i in range(len(nodes)):
        if i%2 != 1:
            result.append(nodes[i])
            tempnode.append(nodes[i])
    for temp in tempnode:
        nodes.remove(temp)

for i in range(level):
    temp = list()
    ptemp = ""
    for _ in range(2**(i)):
        temp.append(result.pop())
    for _ in range(len(temp)):
        
        ptemp = ptemp+str(temp.pop())+" "
    print(ptemp)