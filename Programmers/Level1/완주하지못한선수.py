# 리스트를 비교하고 없는 데이터 찾는 문제
# collections.Counter를 사용하면 매우 쉽게 풀이 가능하다. 하지만 전 문제에서 사용했던 zip을 사용해서 풀어보았다.
# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant.sort()
    completion.sort()
    # comp의 길이에 맞춰서 튜플이 생성됨
    for part, comp in zip(participant, completion):
        if part != comp:
            return part
    # 모두 같다면 마지막 part가 미완주자    
    return participant[-1]