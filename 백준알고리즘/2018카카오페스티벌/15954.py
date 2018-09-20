strnum = input().split(" ")
dullNum = int(strnum[0])
selectSize = int(strnum[1])
likeNum = input().split(" ")
m = 0
flag = False
for i in range(dullNum - selectSize+1):
    tempsum= 0
    temp2 = 0
    for k in range(dullNum-selectSize-i+1):
        for temp in range(selectSize+k):
            tempsum += int(likeNum[temp+i])
        
        m = tempsum/(selectSize+k)
        for temp in range(selectSize+k):
            temp2 += (int(likeNum[temp+i])-m)**2

        tempv = (temp2/(selectSize+k))**0.5
        if not flag:
            flag = True
            v = tempv
        if tempv<v:
            v = tempv
print(v) 
    