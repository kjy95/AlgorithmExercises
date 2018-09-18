import sys

n, m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n + 1)]

def find(elm1):
    if parents[elm1]==elm1:
        return elm1
    else :
        parents[elm1] = find(parents[elm1])
        return parents[elm1]

def union(elm1, elm2):
    if find(elm1)!=find(elm2):
        parents[find(elm1)] = (elm2)

for _ in range(m):
    x, elm1, elm2 = map(int, sys.stdin.readline().split())
    if x == 0:
        union(elm1, elm2)
    else:
        if find(elm1) == find(elm2):
            print("YES\n")
        else:
            print("NO\n")
            
#sys.stdin.readline().split()로 안하고 input()으로 하면 시간초과남
#Disjoint Algorithm 사용