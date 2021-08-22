# https://www.acmicpc.net/problem/1260
"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""
import sys
from collections import deque
input = sys.stdin.readline


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)

# DFS로 visit이 1로 세팅되었으므로 반대로 방문시 0으로 표시한다.
def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i] == 1 and graph[v][i] == 1:
                q.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(v)
print()
bfs(v)
