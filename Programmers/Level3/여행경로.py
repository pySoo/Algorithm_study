#
"""
문제
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

입출력
tickets	/ return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	/ ["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]   /	 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
"""
"""
알고리즘
1. {시작점: [도착점], ...} 형태의 도착점들을 정렬한 인접 리스트 생성
2. DFS 알고리즘 사용 모든 노드 순회
2-1. 현재 노드가 그래프에 있으며 티켓을 모두 사용한 경우가 아닐경우
가장 앞 데이터를 stack에 저장
2-2. 2-1이 아닌경우 티켓을 모두 사용했으므로 route에 저장
3. route 역순 출력
"""




from collections import defaultdict
def solution(tickets):
    answer = []
    path = defaultdict(list)
    # 1
    for a, b in sorted(tickets):
        path[a].append(b)

    stack, route = ['ICN'], []
    # 2
    while stack:
        now = stack[-1]
        # 2-1
        if now in path and len(path[now] != 0):
            stack.append(path[now].pop(0))
        # 2-2
        else:
            route.append(stack.pop())
    # 3
    return route[::-1]
