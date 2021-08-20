# https://www.acmicpc.net/problem/2745
"""
문제
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.
"""
import sys
input = sys.stdin.readline
n, b = map(int, input().split())
n = n[::-1]
sum = 0
abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(n)):
    # 자리수 * 진수 + 나머지
    sum += abc.index(n[i]) * (b ** i)

print(sum)
