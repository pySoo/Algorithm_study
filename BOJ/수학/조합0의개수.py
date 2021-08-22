# https://www.acmicpc.net/problem/2004
"""
문제
nCm의 끝자리 의 개수를 출력하는 프로그램을 작성하시오

입력
첫째 줄에 정수 n, m (0<=m<=n<=2,000,000,000) 이 들어온다.

출력
첫째 줄에 nCm의 끝자리 0의 개수를 출력한다.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


def five_count(n):
    answer = 0
    while n != 0:
        n //= 5
        answer += n
    return answer


def two_count(n):
    answer = 0
    while n != 0:
        n //= 2
        answer += n
    return answer


# n!이 가지고 있는 2의 개수 - (m-n)!이 가지고 있는 2의 개수 - m!이 가지고 있는 2의 개수
# 5의 개수도 마찬가지
print(min(two_count(n) - two_count(n-m) - two_count(m),
      five_count(n) - five_count(n-m) - five_count(m)))
