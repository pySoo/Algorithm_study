# https://www.acmicpc.net/problem/1780
"""
문제
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 3^7, N은 3^k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
"""
import sys
imput = sys.stdin.readline

n = int(input())
matrix = []
result = [0] * 3

for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 모두 같은 수인지 체크하는 함수


def check(x, y, n):
    val = matrix[x][y]
    for i in range(n):
        for j in range(n):
            # 모두 같은 수가 아님
            if val != matrix[x+i][y+j]:
                return False
    return True


def divide(x, y, n):
    # 모두 같은 수일 때
    if check(x, y, n):
        # 매트릭스 값은 -1,0,1 Result 인덱스는 0,1,2이므로 1을 더해준다
        result[matrix[x][y] + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + i * n // 3, y + j * n // 3, n // 3)


divide(0, 0, n)
for i in range(3):
    print(result[i])
