a = input()

i = int(a)
array = list()

while i > 0:
    temp = input()
    array.append(temp)
    i -= 1

array.sort()
array.reverse()
i = 1
temp2 = ""
while i <= 50:
    temp =  int(a)

    while temp > 0:
        if temp2 != array[temp-1] and (len(array[temp-1]) == i):
            
            print(array[temp-1])
            temp2 = array[temp-1]
            
        temp -= 1  
    i += 1

#30684kb 1312ms 422b