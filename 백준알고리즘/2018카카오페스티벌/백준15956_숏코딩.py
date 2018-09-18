#input using map()
#how to use map? --> map(f, iterable) f:funtion, iterable: iterable value
and_list= list(map(str, input().split("&&")))
pvot = 1

equal_list = [[[0]*1000000 for i in range(1000000)]]
result_list = []
for i in range(len(and_list)):
    if and_list.count("==")>0:
        temp_list = and_list[i].split("==")
        print(temp_list)
    if temp_list[0] == temp_list[1]:
        equal_list.append(temp_list[0:]) 
    nonequal_list = and_list[i].split("!=")
    result_list.append(nonequal_list[0:]+"&&")