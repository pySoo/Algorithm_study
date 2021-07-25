# https://www.acmicpc.net/problem/7576
# 위 문제는 인접 노드가 1인 것들을 탐색하는 것이 아니라, 1인 노드들이 주변 0노드를 1로 만드는 문제이기 떄문에
# 큐에 값이 1인 노드를 넣고 주변 노드를 방문하도록 시작하는 것이 중요하다.
# 방문시마다 maps에 1을 더해서 최대값을 구하면 최종 몇 번 방문했는지 알 수 있다.
# 즉, 방문한 최대값이 토마토가 모두 익는데 걸린 날짜이다. 단, 익은 것들을 1일로 카운트 했기 때문에 -1 연산을 한다.
"""
문제
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.  며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

출력
토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
"""
from collections import deque
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ripe = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bfs():
    while ripe:
        x, y = ripe.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    ripe.append((nx, ny))

    result = -1
    for row in maps:
        # 안 익은 토마토가 있기 때문에 -1을 출력한다.
        if 0 in row:
            return -1
        # 행마다 방문 횟수(익는데 걸린 시간)가 가장 큰 값을 result에 저장한다.
        max_day = max(row)
        result = max(result, max_day)

    # 주어질 때부터 모두 익어있는 상태라면 0을 출력
    if result == 1:
        return 0
    else:
        # 아니라면 result 출력, 이미 익어있던 것들을 1일로 카운트 했기 때문에 -1을 더한다.
        return (result-1)


for i in range(n):
    for j in range(m):
        if maps[i][j]:
            ripe.append((i, j))

print(bfs())
