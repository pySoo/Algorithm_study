# https://www.acmicpc.net/problem/11576
"""
문제
뛰어난 프로그래머였던 정이는 A진법으로 나타낸 숫자를 B진법으로 변환시켜주는 프로그램을 작성하기로 한다. 

입력
입력의 첫 줄에는 미래세계에서 사용하는 진법 A와 정이가 사용하는 진법 B가 공백을 구분으로 주어진다. A와 B는 모두 2이상 30이하의 자연수다.
입력의 두 번째 줄에는 A진법으로 나타낸 숫자의 자리수의 개수 m(1 ≤ m ≤ 25)이 주어진다. 세 번째 줄에는 A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다. 각 숫자는 0이상 A미만임이 보장된다. 또한 수가 0으로 시작하는 경우는 존재하지 않는다.
A진법으로 나타낸 수를 10진법으로 변환하였을 때의 값은 양의 정수이며 220보다 작다.

출력
입력으로 주어진 A진법으로 나타낸 수를 B진법으로 변환하여 출력한다.
"""
import sys
input = sys.stdin.readline

# A진법을 B진법으로 변환
a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
ten = 0
answer = []
for i in range(m):
    # A 진법 10진수로 변환
    ten += arr[-1] * a**i
    arr.pop(-1)

while ten > 0:
    answer.append(str(ten % b))
    ten //= b

print(' '.join(answer[::-1]))
