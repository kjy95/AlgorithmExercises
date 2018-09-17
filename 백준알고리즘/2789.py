string = input()
def replace(string, cambridge):
    temp = string.replace(cambridge,"")
    string = temp
    return string

string = replace(string, "C")
string = replace(string, "A")
string = replace(string, "M")
string = replace(string, "B")
string = replace(string, "R")
string = replace(string, "I")
string = replace(string, "D")
string = replace(string, "G")
string = replace(string, "E")
print(string)
#29163kb 72ms 424b
"""
a=input()
t="CAMBRIDGE"
for i in range(len(a)):
    if t.count(a[i])>0:
        continue
    print(a[i],end='')

"""