# 반드시 이웃해 있는 단지들을 이용해 단지 별 가구수를 구하는 문제
# https://www.acmicpc.net/problem/2667

""""
문제>
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력>
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력>
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""


# DFS 풀이
from collections import deque
n = int(input())
maps = [list(map(int, input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = []


def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if maps[i][j] and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
print('\n'.join(map(str, answer)))


# BFS 풀이
n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j, cnt):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    # 인접 아파트마다 개수를 카운트 한다.
                    apt_list[cnt] += 1


apt_list = {}
cnt = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] and not visited[i][j]:
            # cnt=단지 수, 해당 단지에 속한 배열마다 visited에 cnt를 저장한다.
            apt_list[cnt] = 1
            bfs(i, j, cnt)
            cnt += 1
apt_list = sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)
