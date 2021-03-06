# https://programmers.co.kr/learn/courses/30/lessons/49189
"""
문제
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

입출력
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
"""
"""
알고리즘
1. 그래프 배열에 graph[a] = [b,...]의 형태로 연결된 노드 추가
2. [정점, 거리]가 저장된 큐의 원소가 없어질 때까지 반복
3. 방문하지 않았다면 방문 배열에 거리를 저장
4. 해당 정점에 연결된 노드들을 큐에 삽입
"""




from collections import deque
def bfs(v, visited, graph):
    cnt = 0
    q = deque([[v, cnt]])
    # 2
    while q:
        x, cnt = q.popleft()
        # 3
        if visited[x] == -1:
            visited[x] = cnt
            cnt += 1
            # 4
            for e in graph[x]:
                q.append([e, cnt])


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    # 1
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    bfs(1, visited, graph)
    for val in visited:
        if val == max(visited):
            answer += 1
    return answer
