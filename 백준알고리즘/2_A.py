import fractions
point = int(input())
listcur = input().split(" ")
startx = int(listcur[0])
starty = int(listcur[1])
tempx = startx
tempy = starty

point_list = [0]*5001
for i in range(point):
    listcur = input().split(" ")
    x = int(listcur[0])
    y = int(listcur[1])
    up = y-tempy 
    down =  x-tempx
    for i in range(x):
        if i >= tempx:
            point_list[i]= fractions.Fraction(int(up),int(down))
    tempx = x
    tempy = y
listcur = input().split(" ")
missionstart = int(listcur[0])
missionend = int(listcur[1])
result = 0
for i in range(missionend-missionstart):
    if i >= missionstart:
        result += point_list[i]
           
b =missionend-missionstart
a = fractions.Fraction(int(result),int(b))
if a<0:
    a = -a
print(a)