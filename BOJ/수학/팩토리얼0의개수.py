# https://www.acmicpc.net/problem/1676
"""
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())

factorial = [1 for _ in range(n+1)]
for i in range(1, n+1):
    factorial[i] = i * factorial[i-1]

answer = 0
flag = 1
while flag:
    if factorial[n] % 10 == 0:
        factorial[n] //= 10
        answer += 1
    else:
        flag = 0

print(answer)
