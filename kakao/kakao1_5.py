A = input()
B = input()
A_list = list()
B_list = list() 
countU = 0
countC = 0
for i in range(int(len(A)-1)):
    temp = A[i]+A[i+1]
    if temp.isalpha():
        temp = temp.lower()
        A_list.append(temp)

for i in range(int(len(B)-1)):
    temp = B[i]+B[i+1]
    if temp.isalpha():
        temp = temp.lower()
        B_list.append(temp)

countU = len(A_list)+len(B_list)
print(A_list)
print(B_list)
for tempstrA in A_list:
    for tempstrB in B_list:
        if tempstrA == tempstrB:
            B_list.remove(tempstrA)
            print(B_list)
            countC += 1
            break
print(B_list)
print(A_list)
countU -= (countC)
if countC == 0 or countU == 0:
    result = 1*65536
else :
    result = (countC/countU)*65536
print(countC)
print(countU)
print(int(result)) 
