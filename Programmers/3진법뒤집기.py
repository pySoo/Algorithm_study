# 주어진 수를 3진법 상에서 앞뒤로 뒤집은 후 10진법으로 표현하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = ''
    while n >= 1:
        # n을 3으로 나눈 몫과 나머지 > 순서대로 계산한 것이 3진법의 역순과 같음
        n, rest = divmod(n,3)
        answer += str(rest)
    # 파이썬 int 함수는 진법 변환을 지원한다.. 우와
    return int(answer,3)