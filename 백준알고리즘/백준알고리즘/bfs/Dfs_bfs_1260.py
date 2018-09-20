N = int(input())
M = int(input())
V = int(input())
M_list = list()
visited_node = [False] * 10001

for i in range(M):
    temp = input()
    temp_list = temp.split(" ")
    temp_list[0]
    M_list.append({"depth":temp_list[0], "nextnode" : temp_list[1]})
    print(M_list)

#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 한 간선이 여러 번 주어질 수도 있는데, 간선이 하나만 있는 것으로 생각하면 된다. 입력으로 주어지는 간선은 양방향이다.
#첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
