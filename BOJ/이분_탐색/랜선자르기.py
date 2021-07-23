# 앞서 풀었던 나무자르기와 비슷한 문제, 랜선을 잘라서 목표치 이상의 개수를 만드는 문제
# https://www.acmicpc.net/problem/1654
from sys import stdin
read = stdin.readline

k, n = map(int, read().split())
lans = []
for i in range(k):
    lans.append(int(read()))

start, end = 1, max(lans)
while start <= end:
    mid = (start+end) // 2
    rest = 0
    for lan in lans:
        rest += lan // mid
        print(rest)
    # 목표치 이상이면 크기를 더 크게 두고 잘라야 함
    if rest >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
