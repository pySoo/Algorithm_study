# https://www.acmicpc.net/problem/10844
"""
문제
인접한 모든 자리수의 차이가 1이 나는 수를 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
"""
import sys
input = sys.stdin.readline
n = int(input())
# 2차원 배열을 만들어서 앞 자리는 몇 번째 자리인지를 뜻하고 뒷 자리는 해당 숫자의 계단 수를 뜻한다.
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    # 첫 째 자리에서 만들 수 있는 수
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            # 0과 차이나는 수는 1밖에 없다.
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)
