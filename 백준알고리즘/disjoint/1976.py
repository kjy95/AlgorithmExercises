import sys
n = int(input())
m = int(input())
cities= [i for i in range(n+1)]

def find(x):
    if cities[x] == x:
        return x
    else:
        cities[x]=find(cities[x])
        return cities[x]

def union(el1, el2):
    if find(el1)!=find(el2): 
        cities[find(el1)] = el2

def check():
    temp = find(can_trip_cities[0])
    for city in can_trip_cities:
        if temp != find(city):
            print("NO")
            return
    print("YES")

for i in range(1, n+1):
    tempcities = list(map(int, sys.stdin.readline().split()))
    for j in range(1,n+1):
        if tempcities[j-1] == 1:
            if find(cities[j]) != find(cities[i]):
                union(cities[j],cities[i])


can_trip_cities = list(map(int, sys.stdin.readline().split()))
check()

