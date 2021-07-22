# 주어진 숫자 배열의 부호를 다르게 해서 target 값을 얻을 수 있는 경우의 개수를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/43165
# nonlocal에 대해 배웠습니다. 전역 변수가 아닌 지역 변수를 다른 scope에서 사용하려면
# nonlocal로 선언을 해야합니다. answer을 global로 설정한 경우 전역 변수가 아니기 때문에 not defined 에러가 발생합니다.

# DFS 풀이
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def DFS(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
                DFS(idx+1, result+numbers[idx])
                DFS(idx+1, result-numbers[idx])
    DFS(0,0)
    return answer

# BFS 풀이
# from collections import deque

# def solution(numbers, target):
#     answer = 0
#     stack = deque([(0,0)])
#     while stack:
#         result, idx = stack.popleft()
#         if idx == len(numbers):
#             if result == target:
#                 answer += 1
#         else:
#             stack.append((result+numbers[idx], idx+1))
#             stack.append((result-numbers[idx], idx+1))
    
#     return answer