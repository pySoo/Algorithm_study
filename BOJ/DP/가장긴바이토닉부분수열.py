# https://www.acmicpc.net/problem/11054
"""
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
"""
# 계속 증가하는 부분과, 감소하는 부분을 구분해야 한다.
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)

arr.reverse()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

decrease.reverse()
for i in range(n):
    dp[i] = increase[i] + decrease[i] - 1
print(max(dp))
