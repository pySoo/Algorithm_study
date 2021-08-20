# https://www.acmicpc.net/problem/2609
"""
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
"""
import sys
input = sys.stdin.readline
a, b = map(int, input().split())

# 유클리드 호제법: 더 작은 수 b와 a%b의 최대공약수와 같다.
# gcd(24, 18)= gcd(18,6)= gcd(6,0)
while b > 0:
    a, b = b, a % b

# 최대 공약수
print(a)
print((a*b) // a)
