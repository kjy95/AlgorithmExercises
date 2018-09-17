testcase = int(input())

for i in range(testcase):
    listcur = input().split(" ")
    firstRank = int(listcur[0])
    secondRank = int(listcur[1])
    firstMoney = 0
    secondMoney = 0

    if firstRank<0 or firstRank>21:
        firstMoney = 0
    elif firstRank == 1:
        firstMoney = 5000000
    elif firstRank > 1 and firstRank <= 3:
        firstMoney = 3000000
    elif firstRank > 3 and firstRank <= 6:
        firstMoney = 2000000
    elif firstRank > 6 and firstRank<=10:
        firstMoney = 500000
    elif firstRank > 10 and firstRank<=15:
        firstMoney = 300000
    elif firstRank > 15 and firstRank<=21:
        firstMoney = 100000
    
    if secondRank<0 or secondRank>31:
        secondMoney = 0
    elif secondRank == 1:
        secondMoney = 5120000
    elif secondRank > 1 and secondRank <= 3:
        secondMoney = 2560000
    elif secondRank > 3 and secondRank <= 7:
        secondMoney = 1280000
    elif secondRank > 7 and secondRank<=15:
        secondMoney = 640000
    elif secondRank > 15 and secondRank<=31:
        secondMoney = 320000
    print(secondMoney+firstMoney)
    
