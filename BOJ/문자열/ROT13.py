# https://www.acmicpc.net/problem/11655
"""
문제
ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

출력
첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
"""
import sys
input = sys.stdin.readline
line = input()
answer = ''
for s in line:
    if 'a' <= s <= 'z':
        # m이 13번째 알파벳이므로 14번째 알파벳부터는 13을 빼준다
        answer += chr((ord(s)+13) if s <= 'm' else ord(s)-13)
    elif 'A' <= s <= 'Z':
        answer += chr((ord(s)+13) if s <= 'M' else ord(s)-13)
    else:
        answer += s
print(answer)
