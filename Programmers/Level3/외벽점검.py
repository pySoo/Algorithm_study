# https://programmers.co.kr/learn/courses/30/lessons/60062
"""
- 문제
레스토랑을 운영하고 있는 "스카피"는 레스토랑 내부가 너무 낡아 친구들과 함께 직접 리모델링 하기로 했습니다. 레스토랑이 있는 곳은 스노우타운으로 매우 추운 지역이어서 내부 공사를 하는 도중에 주기적으로 외벽의 상태를 점검해야 할 필요가 있습니다.
레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있습니다. 따라서 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는 지, 주기적으로 친구들을 보내서 점검을 하기로 했습니다. 다만, 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한했습니다. 친구들이 1시간 동안 이동할 수 있는 거리는 제각각이기 때문에, 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사를 돕도록 하려고 합니다. 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다. 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다.
외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성해주세요.

- 제한사항
n은 1 이상 200 이하인 자연수입니다.
weak의 길이는 1 이상 15 이하입니다.
서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
weak의 원소는 0 이상 n - 1 이하인 정수입니다.
dist의 길이는 1 이상 8 이하입니다.
dist의 원소는 1 이상 100 이하인 자연수입니다.
친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.
"""
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    l = len(weak)
    candidate = []
    # 배열을 2배 늘려서 반시계를 반영
    weak_point = weak + [w+n for w in weak]
    for i, start in enumerate(weak):
        # 친구들의 dist를 순열로 (1,2,3,4)
        for friends in permutations(dist):
            cnt = 1
            # 현위치
            pos = start
            for distance in friends:
                # 친구 거리만큼 이동
                pos += distance
                # 끝 포인트까지 못간경우
                if pos >= weak_point[i+l-1]:
                    answer = min(answer, cnt)
                else:
                    # 현위치보다 큰 첫 좌표를 현위치로
                    # 이미 지났으면 cnt 늘릴 필요가 없다
                    pos = [w for w in weak_point if w > pos][0]
                    cnt += 1
    # 초기 answer을 친구수로 설정, 이보다 크다면 -1 리턴
    return answer if answer <= len(dist) else -1
