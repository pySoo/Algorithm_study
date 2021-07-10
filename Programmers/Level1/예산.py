# 총예산에 맞도록 d 배열에 있는 예산 값을 조합하여 최대한 많은 부서를 선택하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        if money <= budget:
            answer += 1
            budget -= money
        else:
            break
        
    return answer