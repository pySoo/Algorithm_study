# https://www.acmicpc.net/problem/1463

n = int(input())
# 0,1,2,3의 최소 연산 수
dp = [0, 0, 1, 1]

for i in range(4, n+1):
    # 먼저 1을 밴 이후에 나누기 2, 나누기3의 연산과 비교한다.
    dp.append(dp[i-1]+1)
    print(dp)
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
        print(dp)
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
print(dp[n])
