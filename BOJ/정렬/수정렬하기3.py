# https://www.acmicpc.net/problem/10989
"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
# 위 문제는 간단한 정렬 문제처럼 보이지만, 메모리 제한과 시간 제한을 해결하는 것이 관건인 문제이다.
import sys
input = sys.stdin.readline
# 입력 숫자의 범위가 0부터 10,000이므로 0으로 가득찬 길이 10,000인 리스트를 생성한다.
check = [0] * 10001
n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    # 입력받은 숫자의 인덱스 값에 1을 추가한다.
    check[num] += 1

for i in range(10001):
    if not check[i]:
        for j in range(check[i]):
            print(i)
