# https://www.acmicpc.net/problem/10866
"""
문제
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    order = input().split()
    command = order[0]
    if command == 'push_front':
        dq.appendleft(int(order[1]))

    elif command == 'push_back':
        dq.append(int(order[1]))

    elif command == 'pop_front':
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if len(dq):
            print(dq.pop())
        else:
            print(-1)

    elif command == 'size':
        print(len(dq))

    elif command == 'empty':
        if len(dq):
            print(0)
        else:
            print(1)

    elif command == 'front':
        if len(dq):
            print(dq[0])
        else:
            print(-1)

    elif command == 'back':
        if len(dq):
            print(dq[-1])
        else:
            print(-1)
