# 해시와 경우의 수를 이용하여 입을 수 있는 경우의 수를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42578
# 딕셔너리에 타입을 키로 정하고, 가진 옷 개수를 value로 설정했습니다.  타입별 옷 개수 + 1(입지 않는 경우)하고 타입마다의 경우의 수를 곱한 다음
# 모두 안 입는 경우 1을 빼서 최종값을 구했습니다.
from collections import defaultdict

def solution(clothes):
    answer = 1
    dicts = {}
    for cloth, types in clothes:
        if types not in dicts:
            dicts[types] = 2
        else:
            dicts[types] += 1
    
    for num in dicts.values():
        answer *= num
        
    return answer - 1