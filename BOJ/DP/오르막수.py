# https://www.acmicpc.net/problem/11057
"""
문제
수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.
(인접한 수가 같아도 오름차순으로 친다.)

입력
첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

출력
첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.
"""
import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        # 해당 숫자보다 적은 숫자의 자리수를 모두 더한다.
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[n]) % 10007)
