# 노드로 연결된 컴퓨터 중에서 한 컴퓨터로 인해 바이러스에 걸린 컴퓨터 수를 구하는 문제
# https://www.acmicpc.net/problem/2606

# 1> DFS 풀이
from sys import stdin
read = stdin.readline
dic = {}

# 숫자를 n = int(read())로 따로 받지 않고 range()안에서 선언해서 범위를 설정할 수도 있습니다.
# 컴퓨터 수만큼 dictionary key 초기화, value를 set()으로 설정
for i in range(int(read())):
    dic[i+1] = set()

for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

# 방문하지 않았다면 해당 노드를 방문합니다.


def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)


visited = []
dfs(1, dic)
# A 컴퓨터로 인해 걸리는 컴퓨터 수를 구하므로 1을 제외해야 합니다.
print(len(visited)-1)

# 2> BFS 풀이
read = stdin.readline
dic = {}

for i in range(int(read())):
    dic[i+1] = set()

for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)


def bfs(start, dic):
    queue = [start]
    while queue:
        num = queue.pop()
        for i in dic[num]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


visited = []
bfs(1, dic)
print(len(visited)-1)
