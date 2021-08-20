# https://www.acmicpc.net/problem/9613
"""
문제
https://www.acmicpc.net/problem/9613

입력
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

출력
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
"""
import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


for _ in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    sum = 0
    for a, b in combinations(arr, 2):
        sum += gcd(a, b)
    print(sum)
