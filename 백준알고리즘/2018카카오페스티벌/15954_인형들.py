import math

#input using map()
#how to use map? --> map(f, iterable) f:funtion, iterable: iterable value

def mean(arr):
    return sum(arr)/len(arr)

def v(arr):
    v = 0
    m = mean(arr)
    for elm in arr:
        v += (elm - m)**2
    v = v/len(arr)
    return v

def std(arr):
    return v(arr)**0.5

def solution():
    stds = []
    n, k = map(int, input().split(" "))
    likes = list(map(int, input().split(" ")))
    for i in range(n-k+1):
        for j in range(i+k,n+1):
            stds.append(std(likes[i:j+1]))
    print(min(stds))
solution()

#31500kb , 680ms
#Python으로 구현하는 경우, 다른 언어들에 비해 실행 시간이 더 걸리기 때문에
# , O(N3) 풀이를 구현하면 시간 초과를 받게 될 수 있습니다.