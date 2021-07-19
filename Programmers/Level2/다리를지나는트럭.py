# 스택을 이용해 트럭이 건너는 최소 시간을 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리를 건너는 트럭
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        # pop(0)을 이용하여 맨 앞의 원소를 제거할 수 있습니다.
        trucks_on_bridge.pop(0)
        # 대기 트럭이 있는 경우
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer