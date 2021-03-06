# https://www.acmicpc.net/problem/1850
"""
문제
모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다. 이때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.
예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고, A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.

입력
첫째 줄에 두 자연수 A와 B를 이루는 1의 개수가 주어진다. 입력되는 수는 263보다 작은 자연수이다.

출력
첫째 줄에 A와 B의 최대공약수를 출력한다. 정답은 천만 자리를 넘지 않는다.
"""
# 자연수의 범위가 2^63이므로 유클리드 호제법으로 구하면 당연히 메모리 에러가 발생한다..
# 아이디어가 생각이 안 나서 다른 분의 풀이를 참고하였다.
# 계산을 하다보면 주어진 크기의 최대 공약수만큼 1이 존재한다는 규칙을 발견할 수 있다.
import sys
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
x, y = (a, b) if a > b else (b, a)
print('1' * gcd(a, b))
