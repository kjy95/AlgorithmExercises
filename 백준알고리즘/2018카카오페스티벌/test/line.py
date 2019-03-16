#1
n = int(input()) 
result = -1
for i in range(1 , (n//2)+2):
    w = n//i 
    h = n//w
    
    if w * h == n and result == -1: 
        result = abs(w-h)
    elif w * h == n :
        temp = abs(w-h)
        result = min(temp, result )   
    
    
print(result)
#2
import re
chStr = input()
numbers = re.findall("\d+", chStr)  
numberList = list(numbers[0])
p = re.compile("[^0-9]")
chStr="".join(p.findall(chStr))

divChStr = chStr[0]

for idx, char in enumerate(chStr[1:]):
    if chStr[idx].islower() and char.isupper():
        divChStr += '-'
    elif chStr[idx].isupper() and char.isupper():
        divChStr += '-'
    divChStr += char
chList = divChStr.split('-')
if len(chList) != len(numberList):
    print("error")
else:
    answer = ""
    for i in range(len(chList)):
        answer += chList[i]
        if numberList[i] != "1" :
            answer += numberList[i]
    print(answer)
#4
import sys
n = int(input())
bulidingHList =  list()
result = -1
for _ in range(n):
    bulidingHList.append(int(sys.stdin.readline().rstrip()))
    
for pivotBuilding in range(n):
    pivot = bulidingHList[pivotBuilding] 
    for otherBuilding in range(pivotBuilding+1, n):
        
        if pivot <= bulidingHList[otherBuilding] and result == -1:
            result = abs(pivotBuilding-otherBuilding)
            #print(result)
            break
        elif pivot <= bulidingHList[otherBuilding] : 
            temp = abs(pivotBuilding-otherBuilding)
            result = max(temp, result)
            break
#print(bulidingHList) 
print(result)