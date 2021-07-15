# 짝수인 경우와 홀수인 경우 계산을 다르게 해서 1을 만드는데 필요한 연산 개수를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    while num > 1:
        num = num * 3 + 1 if num % 2 != 0 else num / 2
        answer += 1
    return answer if answer < 500 else -1