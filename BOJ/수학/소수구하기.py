# https://www.acmicpc.net/problem/1929
"""
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""
# 전체 범위에서 비교하면 시간 초과가 발생하기 때문에
# 에라토스테네스의 체를 사용하였다.
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
answer = []


def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


for i in range(m, n+1):
    if isPrime(i):
        print(i)
