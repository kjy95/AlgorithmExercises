import sys

testcase = int(sys.stdin.readline())
 
for _ in range(testcase):
    PhoneNum_Num =int(sys.stdin.readline())
    PhoneNums = list()
    for i in range(PhoneNum_Num):
        PhoneNums.append(sys.stdin.readline().rstrip())
    PhoneNums.sort()
    flage = False
    for i in range(PhoneNum_Num):
        if i==0:
            if(PhoneNums[i].startswith(PhoneNums[i+1])):
                flage = True
                break
        elif i==PhoneNum_Num-1:
            if (PhoneNums[i].startswith(PhoneNums[i-1])):
                flage = True
                break 
        else :
            if (PhoneNums[i].startswith(PhoneNums[i-1]))or(PhoneNums[i].startswith(PhoneNums[i+1])):
                flage = True
                break 
        if flage:
            break
    if flage:
        print("NO")
    else:   
        print("YES") 
        

