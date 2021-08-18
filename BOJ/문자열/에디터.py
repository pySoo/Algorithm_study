# https://www.acmicpc.net/problem/1406
"""
문제
초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

입력
첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

출력
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
"""
import sys
input = sys.stdin.readline

# 문자열 슬라이싱을 사용하면 시간 초과가 발생해서 커서를 기준으로 왼쪽 스택, 오른쪽 스택으로 구분하여 풀어야 한다.
stack1 = list(input().strip('\n'))
stack2 = []
m = int(input())
for _ in range(m):
    order = input().split()
    if order[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif order[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif order[0] == 'B':
        if stack1:
            stack1.pop()
    elif order[0] == 'P':
        stack1.append(order[1])
print(''.join(stack1+list(reversed(stack2))))
