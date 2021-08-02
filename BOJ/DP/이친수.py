# https://www.acmicpc.net/problem/2193
"""
문제
이친수는 다음의 성질을 만족한다.
이친수는 0으로 시작하지 않는다.
이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다.

출력
첫째 줄에 N자리 이친수의 개수를 출력한다.
"""
import sys
input = sys.stdin.readline

# 경우의 수를 나열하면 n-1, n-2번째 결과의 합이 n번째 결과이다.
n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
