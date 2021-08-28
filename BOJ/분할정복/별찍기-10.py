# https://www.acmicpc.net/problem/2447
"""
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
"""
import sys
input = sys.stdin.readline


def draw_star(n):
    global map

    if n == 3:
        map[0][:3] = map[2][:3] = ['*'] * 3
        map[1][:3] = ['*', ' ', '*']
        return
    div = n // 3
    draw_star(div)
    for i in range(0, n, div):
        for j in range(0, n, div):
            if i != div or j != div:
                for k in range(div):
                    map[i+k][j:j+div] = map[k][:div]


n = int(input())
map = [[' ' for _ in range(n)] for _ in range(n)]
draw_star(n)

for i in range(n):
    for j in range(n):
        print(map[i][j], end='')
    print()
