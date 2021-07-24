# https://www.acmicpc.net/problem/1012
"""
문제
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
배추가 군데군데 심어진 배추밭에서 필요한 흰지렁이 수를 구하라
"""

t = int(input())
m, n, k = map(int, input().split())
maps = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(k):
    a, b = map(int, input().split())
    maps[b][a] = 1


def dfs(x, y):
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny]:
                dfs(nx, ny)


cnt = 0
for i in range(n):
    for j in range(m):
        if maps[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)
