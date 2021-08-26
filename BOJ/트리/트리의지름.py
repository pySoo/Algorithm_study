# https://www.acmicpc.net/problem/1167
"""
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ v   ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.
먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.
"""
import sys

v = int(sys.stdin.readline())

matrix = [[] for _ in range(v + 1)]
for _ in range(v):
    path = list(map(int, sys.stdin.readline().split()))
    path_len = len(path)
    for i in range(1, path_len//2):
        matrix[path[0]].append([path[2*i-1], path[2*i]])


# 첫번째 dfs결과
result1 = [0 for _ in range(v + 1)]


def dfs(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start]+d
            dfs(e, matrix, result)


dfs(1, matrix, result1)
# 루트노드가 정해져 있지않아 양방향으로 입력을 받기때문에 해당
result1[1] = 0

# 최대값 구하기
tmpmax = 0
# 최장경로 노드
index = 0

for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

# 최장경로 노드에서 다시 dfs를 통해 트리지름구하기
result2 = [0 for _ in range(v + 1)]
dfs(index, matrix, result2)
result2[index] = 0
print(max(result2))
