# https://www.acmicpc.net/problem/10451
"""
문제
N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
"""
import sys
sys.setrecursionlimit(2000)  # 최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다


def dfs(x):
    visited[x] = True
    number = numbers[x]  # 다음 방문 장소
    if not visited[number]:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N  # 방문여부확인용
    result = 0

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)
