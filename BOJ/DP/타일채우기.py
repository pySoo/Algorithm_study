# https://www.acmicpc.net/problem/2133
# 아이디어 생각하기가 어려워서 참고한 블로그 https://jyeonnyang2.tistory.com/51
"""
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다.
"""
n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else:
        dp[i] = 0
print(dp[n])
