# n/2개 이하이며 가장 많은 종류의 원소를 선택하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    limit = len(nums) // 2
    sets = set(nums)
    if len(sets) > limit:
        answer = limit
    else:
        answer = len(sets)
    return answer
# 한 줄의 간결한 풀이도 있었다. set 함수가 정말 유용하다.
# return min(len(set(nums)), len(nums)//2)