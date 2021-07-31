# https://www.acmicpc.net/problem/2512

"""
문제
정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

입력
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다.
그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 

출력
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 
"""
# 이분 탐색 활용 기본 문제, 이제 이분 탐색 활용법에 대한 감을 잡은 것 같다.

n = int(input())
budget = list(map(int, input().split()))
m = int(input())
start, end = 0, max(budget)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for money in budget:
        sum += min(money, mid)
    if sum > m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
