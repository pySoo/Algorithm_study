# 두 수를 뽑아 더해서 중복없는 값을 오름차순으로 배열한 배열을 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations

def solution(numbers):
    answer = []
    combi = list(combinations(numbers,2))
    for n1, n2 in combi:
        sums = n1+n2
        if sums not in answer:
            answer.append(sums)
    answer.sort()
    
    return answer