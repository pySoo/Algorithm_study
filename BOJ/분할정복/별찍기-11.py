# https://www.acmicpc.net/problem/2448
"""
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N이 주어진다. N은 항상 3×2^k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
"""
import math
import sys
input = sys.stdin.readline

answer = ["  *  ", " * * ", "*****"]


def stars(space):
    length = len(answer)
    for i in range(length):
        answer.append(answer[i], answer[i])
        answer[i] = ("   " * space + answer[i] + "   " * space)


n = int(input())
iterate = int(math.log(n//3, 2))
for i in range(iterate):
    stars(int(pow(2, i)))

for i in range(n):
    print(answer[i])
