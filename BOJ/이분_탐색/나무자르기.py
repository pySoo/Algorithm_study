# 최소 m미터의 나무를 가져가기 위해 설정할 수 있는 절단기의 최대 높이를 구하는 문제
# https://www.acmicpc.net/problem/2805
# 이분 탐색을 사용하지만 달라지는 점은 while문 안에 나무 배열 for문을 통해 절단 후의 길이를 비교하는 점입니다.
from sys import stdin
read = stdin.readline
n, m = map(int, read().split())
tree = list(map(int, read().split()))

start = 1
end = max(tree)
while start <= end:
    mid = (start + end) // 2
    rest = 0
    for n in tree:
        if n >= mid:
            rest += n - mid

    if rest >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
