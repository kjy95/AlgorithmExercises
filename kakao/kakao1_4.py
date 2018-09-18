#셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m
n = int(input())
t = int(input())
m = int(input())
timetable_size = int(input("timetablesize"))
timetable_list = list()
timetable_int_list = list()
linetable = list()#그사람 앞에섬.
#timetable_list/timetable_int_list 설정
for i in range(timetable_size) :
    timetable_list.append(input("timetable"))
    time_lsit_int = timetable_list[i].split(":")
    time_int = time_lsit_int[0]+time_lsit_int[1]
    timetable_int_list.append(int(time_int))
#오름차순 정렬
timetable_int_list.sort()
#아래 포문에서 사용
temp = 0
count_crue = 1
for time_int in timetable_int_list:
    if time_int == temp:
        count_crue += 1
    temp = time_int
    linetable.append(count_crue)

#아래 포문에서 사용
temp_my_line = 0
real_myline = 0
for temp in linetable:
    real_myline = temp_my_line
    if n*t*m < temp_my_line:
        break
    else:
        temp_my_line+=temp
if timetable_int_list[real_myline] == 9:
    print()
timetable_int_list[real_myline] += 1
timetable_list[real_myline][2].append(":")