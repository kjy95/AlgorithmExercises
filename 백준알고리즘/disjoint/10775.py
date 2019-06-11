import sys
gate_num = int(sys.stdin.readline())
plain_num = int(sys.stdin.readline())
flag = False
gList = [0] * (gate_num+1)

for _ in range(plain_num):
    i = int(sys.stdin.readline())
    num = i
    while num > 0:
        if gList[num]==1 and num==1:
            flag = True
        elif gList[num]==0:
            gList[num] = 1
            break
        num -= 1
    if flag ==True:
        break

print(gList.count(1))