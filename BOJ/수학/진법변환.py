# https://www.acmicpc.net/problem/11005
"""
문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.
"""
import sys
input = sys.stdin.readline
n, b = map(int, input().split())
answer = ''
abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while n > 0:
    """
    362(10)= 몫 36, 나머지 2 -> 2 추가
    36(10)= 몫 3, 나머지 6 -> 6 추가
    3(10)= 나머지 3-> 3추가
    정답: 362(순서의 역)
    """
    answer += str(abc[n % b])
    n //= b

print(answer[::-1])
