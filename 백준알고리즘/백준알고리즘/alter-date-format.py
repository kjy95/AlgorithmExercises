import sys
        
class Time24():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second 

    def AddSecond(self, N):
        self.second += N%60
        if self.second>=60:
            self.minute += 1
            self.second = self.second%60

        self.minute += (N/60)%60
        if self.minute >= 60:
            self.hour += 1
            self.minute = self.minute%60

        self.hour += N/(60*60)
        if self.hour >= 24:
            self.hour = self.hour%24

    def FloatToIntToStringAndSetDigit2(self):
        self.second = str(int(self.second))
        self.minute = str(int(self.minute))
        self.hour = str(int(self.hour))

        self.second = setDigit2String(self.second)
        self.minute = setDigit2String(self.minute)
        self.hour = setDigit2String(self.hour)

def setDigit2String(string):
    if len(string)< 2:
        return "0" + string
    else:
        return string

def ConvertHour12ToHour24(AmPm, hour):
    if AmPm == "AM":
        if hour == 12:
            return hour-12
        else:
            return hour

    elif AmPm == "PM":
        if hour == 12:
            return hour
        else:
            return hour+12

def solution(time12, N): 
    timeList = time12.split()
    AmPm =  timeList[0]
    time = timeList[1]

    timeList = time.split(":")
    hour12 = timeList[0]
    minute = timeList[1]
    second = timeList[2]

    hour24 = ConvertHour12ToHour24(AmPm, int(hour12))
    
    time24 = Time24(hour24, int(minute), int(second))
    time24.AddSecond(int(N))
    time24.FloatToIntToStringAndSetDigit2()

    addSecResult = str(time24.hour)+":"+str(time24.minute)+":"+str(time24.second)
    return addSecResult

#stdin
print("###test0###")
AmPm,time, N = map(str, sys.stdin.readline().split()) 
time12 = AmPm+' '+time
result = solution(time12, N)
print(result)
#test 
print("###test1###")
result = solution('PM 01:00:00', '10')
print(result)
print("###test2###")
result = solution('PM 11:59:59', '1')
print(result)
print("###test3###")
result = solution('AM 12:10:00', '40')
print(result)
print("###test4###")
result = solution('AM 05:24:03', '102392')
print(result)