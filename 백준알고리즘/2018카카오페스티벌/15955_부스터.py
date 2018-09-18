n, q = map(int, input().split(" "))
xiyi = []
qlist = []
checkx = []
checky = []
visitied = [False]*(n+1)
missionS = 0
missionE = 0 
booster = False 

for i in range(n):
    xiyi = list(map(int, input().split(" ")))
    checkx.append(xiyi[0])
    checky.append(xiyi[1])

for i in range(q):
    qlist = list(map(int, input().split(" ")))
    missionS=(qlist[0])-1
    missionE=(qlist[1])-1 
    hpmax=(qlist[2])  
    hp = hpmax
    
    booster = True
    visitied[missionS]  = True
    if checkx[missionS] == checkx[missionE] and checky[missionS] == checky[missionE]:
       result = "YES"
       booster = False
    
    

       
   