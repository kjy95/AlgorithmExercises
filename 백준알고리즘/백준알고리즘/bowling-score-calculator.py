# 1개임 10프레임/ 1~9번프레임 2회투구, 10번 프레임은 처음 스트라이크와 스페어처리를 하면 3회투구 
# 10핀 볼링 룰 : https://blog.naver.com/lifesewon/90176155368 참고
import sys
class BowlingScore():
    def __init__(self, fallenPinesStrList):#third == bool
        self.frame = 0
        self.fallenPinesStrList = fallenPinesStrList

    def setScore(self):
        self.first = []
        self.second = [] 
        self.secondFlag = False
        self.secondFrameFlag = 0
        for bowlingCount in range(len(self.fallenPinesStrList)-1):
            if self.secondFlag == True: 
                self.secondFlag = False 
                self.second[self.secondFrameFlag ] = self.fallenPinesStrList[bowlingCount]
                continue
            elif self.fallenPinesStrList[bowlingCount] == "A": 
                self.first.append(self.fallenPinesStrList[bowlingCount])
                self.second.append("0")
            else:#first만있고 second가 없으면 0 처리 해줌
                self.first.append(self.fallenPinesStrList[bowlingCount])
                self.second.append("0")
                self.secondFrameFlag = len(self.second)-1
                self.secondFlag = True
    def calScore(self): 
        self.frameTotalScoreList = []
        for frame in range(len(self.first)):
            if self.first[frame] == "A":
                self.frameTotalScoreList.append("STRIKE")
            else:
                self.frameTotalScoreList.append(self.first[frame])
                total = str(int(self.frameTotalScoreList[frame]) + int(self.second[frame]))
                self.frameTotalScoreList[frame] = total
                if self.frameTotalScoreList[frame] == '10':
                    self.frameTotalScoreList[frame] = 'SPARE'

        for frame in range(len(self.frameTotalScoreList)-1):   
            if self.frameTotalScoreList[frame] == "STRIKE":
                if frame+2 < len(self.frameTotalScoreList):
                    bonuseScore = strikeBonuseScore(frame, self.first, self.second)
                    self.sumBonuseScoreFrameScore(frame,bonuseScore) 
                    self.sumBeforeScore(frame) 
            elif self.frameTotalScoreList[frame] == "SPARE":
                if frame+1 <= len(self.frameTotalScoreList)-1:
                    bonuseScore = spareBonuseScore(frame, self.first) 
                    self.sumBonuseScoreFrameScore(frame,bonuseScore) 
                    self.sumBeforeScore(frame) 
            else:
                bonuseScore = 0
                self.sumBeforeScore(frame) 
                  
    def sumBeforeScore(self, frame):
        if frame == 0:
            if self.frameTotalScoreList[frame] =="STRIKE":
                self.frameTotalScoreList[frame] = "10"
        else:
            self.frameTotalScoreList[frame] =  str(int(self.frameTotalScoreList[frame-1])+int(self.frameTotalScoreList[frame]))      

    def sumBonuseScoreFrameScore(self,frame,bonuseScore):
        if self.frameTotalScoreList[frame] == "STRIKE" or self.frameTotalScoreList[frame] == "SPARE":
            self.frameTotalScoreList[frame] = str(10 + int(bonuseScore))
        else:
            self.frameTotalScoreList[frame] = str(int(self.frameTotalScoreList[frame]) + int(bonuseScore))

    def removeSome(self):
        if "STRIKE" in self.frameTotalScoreList:
            self.frameTotalScoreList.remove("STRIKE")
        if "SPARE" in self.frameTotalScoreList:
            self.frameTotalScoreList.remove("SPARE")
        while True:
            if len(self.frameTotalScoreList)>10:
                del self.frameTotalScoreList[len(self.frameTotalScoreList)-1]
            else:
                break
    def findError(self):
        if len(self.first) > 12:
            print("frame error")
            exit()
        elif len(self.first) == 12 :
            if self.first[10] == "A":
                pass
        elif len(self.first) == 11:
            if int(self.first[9])+int(self.second[9]) == 10:
                pass
            else:
                print("frame error")
                exit()
        for frame in range(len(self.first)):
            if self.first[frame] == "A":
                continue
            elif self.second[frame] == "A" or int(self.first[frame]) + int(self.second[frame]) > 10:
                    print("한 프레임 점수가 10 이 넘는 에러")
                    exit()
    def testSetScore(self):
        print(self.first)
        print(self.second)

    def testCalScore(self): 
        print(self.frameTotalScoreList) 

def strikeBonuseScore(frame, first, second):
    nextScore = first[frame+1]
    nextNextScore = 0
    if nextScore == "A":
        nextScore = '10'
        if first[frame+2] == "A":
            nextNextScore = '10'
        else:
            nextNextScore = first[frame+2]
    else:
        if second[frame+1]  == "A":
            nextNextScore = '10'
        else:
            nextNextScore = second[frame+1]  
    return str(int(nextScore) + int(nextNextScore))
def spareBonuseScore(frame, first): 
    nextScore = first[frame+1]
    if nextScore  == "A":
            nextScore = '10'  
    return nextScore
def transScoreStrToInt(fallenPine):
    if fallenPine == "A":
        return 10
    else:
        return int(fallenPine)

fallenPinesStr = sys.stdin.readline()

bowlingScore = BowlingScore(fallenPinesStr)
bowlingScore.setScore()
bowlingScore.findError()
bowlingScore.calScore()
#bowlingScore.testSetScore()
bowlingScore.removeSome()
bowlingScore.testCalScore() 
#AA82AAA91AAAA6
#AA82AAA91AA333 frame error