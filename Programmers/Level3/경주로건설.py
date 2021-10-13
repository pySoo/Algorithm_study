# https://programmers.co.kr/learn/courses/30/lessons/67259
"""
- 문제
건설회사의 설계사인 죠르디는 고객사로부터 자동차 경주로 건설에 필요한 견적을 의뢰받았습니다.
제공된 경주로 설계 도면에 따르면 경주로 부지는 N x N 크기의 정사각형 격자 형태이며 각 격자는 1 x 1 크기입니다.
설계 도면에는 각 격자의 칸은 0 또는 1 로 채워져 있으며, 0은 칸이 비어 있음을 1은 해당 칸이 벽으로 채워져 있음을 나타냅니다.
경주로의 출발점은 (0, 0) 칸(좌측 상단)이며, 도착점은 (N-1, N-1) 칸(우측 하단)입니다. 죠르디는 출발점인 (0, 0) 칸에서 출발한 자동차가 도착점인 (N-1, N-1) 칸까지 무사히 도달할 수 있게 중간에 끊기지 않도록 경주로를 건설해야 합니다.
경주로는 상, 하, 좌, 우로 인접한 두 빈 칸을 연결하여 건설할 수 있으며, 벽이 있는 칸에는 경주로를 건설할 수 없습니다.
이때, 인접한 두 빈 칸을 상하 또는 좌우로 연결한 경주로를 직선 도로 라고 합니다.
또한 두 직선 도로가 서로 직각으로 만나는 지점을 코너 라고 부릅니다.
건설 비용을 계산해 보니 직선 도로 하나를 만들 때는 100원이 소요되며, 코너를 하나 만들 때는 500원이 추가로 듭니다.
죠르디는 견적서 작성을 위해 경주로를 건설하는 데 필요한 최소 비용을 계산해야 합니다.

도면의 상태(0은 비어 있음, 1은 벽)을 나타내는 2차원 배열 board가 매개변수로 주어질 때, 경주로를 건설하는데 필요한 최소 비용을 return 하도록 solution 함수를 완성해주세요.

- 제한사항
board는 2차원 정사각 배열로 배열의 크기는 3 이상 25 이하입니다.
board 배열의 각 원소의 값은 0 또는 1 입니다.
도면의 가장 왼쪽 상단 좌표는 (0, 0)이며, 가장 우측 하단 좌표는 (N-1, N-1) 입니다.
원소의 값 0은 칸이 비어 있어 도로 연결이 가능함을 1은 칸이 벽으로 채워져 있어 도로 연결이 불가능함을 나타냅니다.
board는 항상 출발점에서 도착점까지 경주로를 건설할 수 있는 형태로 주어집니다.
출발점과 도착점 칸의 원소의 값은 항상 0으로 주어집니다.
"""
# 일반 BFS 문제처럼 visited를 T/F로 설정하는 것이 아닌,
# cost로 설정하여 최소 비용을 찾아내는 것이 중요한 문제
# 주의사항: 시작점[0,0]에서 갈 수 있는 경우는 오른쪽/아래의 두 가지 경우가 있다.
# 위 두 경우에 대한 BFS 이동 비용을 비교하여야 테스트 25번을 통과할 수 있다.
from collections import deque


def bfs(board, start):
    n = len(board)
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    answer = 0
    q = deque()
    q.append(start)
    while q:
        x, y, d, c = q.popleft()
        if x == n-1 and y == n-1 and (answer == 0 or answer > c):
            answer = c
        for dx, dy, direction in (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'):
            nx, ny = x + dx, y + dy
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if board[nx][ny]:
                continue
            cost = c + (100 if d == direction else 600)
            if visited[nx][ny] != -1 and visited[nx][ny] < cost:
                continue
            q.append([nx, ny, direction, cost])
            visited[nx][ny] = cost
    return answer


def solution(board):
    return min(bfs(board, [0, 0, 'D', 0]), bfs(board, [0, 0, 'R', 0]))
