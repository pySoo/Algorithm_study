# https://www.acmicpc.net/problem/11656
"""
문제
문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

출력
첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.
"""
import sys
input = sys.stdin.readline

word = input().rstrip()
answer = []
for i in range(len(word)):
    answer.append(word[i:])

for s in sorted(answer):
    print(s)
