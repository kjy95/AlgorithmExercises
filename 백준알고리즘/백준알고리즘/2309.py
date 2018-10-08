import sys
heights = list()
for _ in range(9):
    height =int(sys.stdin.readline())
    heights.append(height)
result =0
flag=0
for i in range(9):
    tempheights = heights.copy()
    tempheights.remove(tempheights[i])
    for k in range(8):
        temptempheights = tempheights.copy()
        temptempheights.remove(temptempheights[k])
        tempresult = sum(temptempheights) 
        if tempresult ==100:
            flag = 1
            break
    if flag ==1:
        break
temptempheights.sort()
for temptempheight in temptempheights:
    print(temptempheight)