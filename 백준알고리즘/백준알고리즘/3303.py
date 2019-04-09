import sys

l = int(sys.stdin.readline())
string = sys.stdin.readline()
length = 0
for i in range(int(l/2)+1):
    print( string.find(string[:i]))
    if string.find(string[:i])!=-1 and length< len(string[:i]):
        length = len(string[:i])
print(length)
