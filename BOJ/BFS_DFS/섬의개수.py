# https://www.acmicpc.net/problem/4963
"""
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
"""
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(i, j):
    s[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and s[x][y] == 1:
                s[x][y] = 0
                queue.append([x, y])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    s = []
    cnt = 0
    for i in range(h):
        s.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
