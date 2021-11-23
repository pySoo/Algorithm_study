# https://programmers.co.kr/learn/courses/30/lessons/42861
"""
- 문제
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.
다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

- 제한사항
섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
"""

"""
크루스칼 알고리즘(최소 신장 트리) 활용 문제
- 탐욕법을 이용하여 가장 적은 비용으로 모든 노드를 연결
1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 최소 비용의 간선을 선택하고 현재의 간선이 사이클을 발생시키는지 확인
2-1. 발생하지 않는 경우 최소 신장 트리에 포함시킴
2-2. 발생하는 경우 포함시키지 않음
3. 방문하지 않은 모든 간선에 대하여 2번 과정을 반복
"""


def solution(n, costs):
    answer = 0
    # 1
    costs.sort(key=lambda x: x[2])
    routes = set([costs[0][0]])
    while len(routes) != n:
        # 2
        for i, cost in enumerate(costs):
            # 2-2 둘 다 집합 안에 있다면 사이클이 존재하기 때문에 재탐색
            if cost[0] in routes and cost[1] in routes:
                continue
            # 2-1 최소 신장트리에 간선을 포함시킴
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                # 해당 값을 다시 사용하지 않기 위함
                costs[i] = [-1, -1, -1]
                break
    return answer
