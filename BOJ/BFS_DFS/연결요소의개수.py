# https://www.acmicpc.net/problem/11724
"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    # (1,2)와 (2,1)는 같은 취급
    graph[x].append(y)
    graph[y].append(x)


def dfs(n):
    visit[n] = 1
    for i in graph[n]:
        if not visit[i]:
            dfs(i)


count = 0
for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        count += 1

print(count)
