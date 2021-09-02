# https://www.acmicpc.net/problem/1451
"""
문제
세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.
세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다. 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.
어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다. 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때, 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다. N과 M은 100보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다. 또, 직사각형에 들어가는 수는 한 자리의 숫자이다.

출력
세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.
"""
n, m = map(int, input().split())

rectangle_input = [[0 for _ in range(m + 1)]]


for _ in range(n):
    line_input = [0] + list(map(int, list(input())))
    rectangle_input.append(line_input)


ans = 0

# 합을 저장할 리스트
s = [[0 for _ in range(m+1)] for _ in range(n+1)]
for row in range(1, n + 1):
    for col in range(1, m + 1):
        s[row][col] = s[row - 1][col] + s[row][col - 1] - \
            s[row - 1][col - 1] + rectangle_input[row][col]


def sum_cal(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]


# 첫번째 경우: 전체 직사각형을 세로로만 분할한 경우
for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3


# 두번째 경우: 전체 직사각형을 가로로만 분할한 경우
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, j, m)
        r3 = sum_cal(j+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 세번째 경우: 전체 세로 분할 후 우측 가로 분할한 경우
for i in range(1, m):
    for j in range(1, n):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, j, m)
        r3 = sum_cal(j+1, i+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 네번째 경우: 전체 세로 분할 후 좌측 가로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 다섯번째 경우: 전체 가로 분할 후 하단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(i+1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 여섯번째 경우: 전체 가로 분할 후 상단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(1, j+1, i, m)
        r3 = sum_cal(i+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

print(ans)
