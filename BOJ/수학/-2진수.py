# https://www.acmicpc.net/problem/2089
"""
문제
10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성하시오.

입력
첫 줄에 10진법으로 표현된 수 N이 주어진다.

출력
-2진법 수를 출력한다.
"""
import sys
input = sys.stdin.readline
n = int(input())
if not n:
    print('0')
    exit()
answer = ''
while n:
    if n % -2:
        answer = '1' + answer
        n = n//-2 + 1
    else:
        answer = '0' + answer
        n //= -2
print(answer)
