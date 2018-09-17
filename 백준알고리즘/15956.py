S = input()
and_list = S.split("&&")
pvot = 1

for i in range(len(and_list)):
    equal_list = and_list[i].split("==")
    nonequal_list = and_list[i].split("!=")