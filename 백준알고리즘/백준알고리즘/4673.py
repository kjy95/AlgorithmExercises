visited = [False]*10001
for i in range(10000):
    length = len(str(i))
    result = i
    for j in range(length):
        result += int(str(i)[j])
    if result<10001:
        visited[result]=True

for i in range(len(visited)):
    if not visited[i]:
        print(i)
  