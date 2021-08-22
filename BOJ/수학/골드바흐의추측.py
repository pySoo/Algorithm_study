# https://www.acmicpc.net/problem/6588
"""
문제
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

입력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
입력의 마지막 줄에는 0이 하나 주어진다.

출력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
입력의 마지막 줄에는 0이 하나 주어진다.
"""
import sys
from itertools import combinations
input = sys.stdin.readline

# 리스트에서 in을 사용할 경우 O(n)이 되므로 boolean 타입의 리스트를 사용해서 O(1)으로 시간 초과를 막았다.
# boolean 타입의 리스트로 미리 소수인 것들을 표시해놓는다.
max = 1000000
check = [True for _ in range(max)]
for i in range(2, int(max**0.5) + 1):
    if check[i] == True:
        for j in range(i+i, max, i):
            check[j] = False

while(True):
    n = int(input())
    if n == 0:
        break
    flag = 0
    for i in range(3, max):
        # 차이가 큰 수를 찾으려 하므로 다음 인자를 n-i로 설정한다.
        if check[i] == True:
            if check[n-i] == True:
                print("%d = %d + %d" % (n, i, n-i))
                flag = 1
                break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
