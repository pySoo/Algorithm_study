# https://www.acmicpc.net/problem/1021
"""
문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
targets = list(map(int, input().split()))
# 숫자 큐
temp = []
for i in range(1, n+1):
    temp.append(i)
queue = deque(temp)

# 왼쪽 원소를 오른쪽에 붙임


def moveLeft(q: deque):
    q.append(q.popleft())
    return queue

# 오른쪽 원소를 왼쪽에 붙임


def moveRight(q: deque):
    q.appendleft(q.pop())
    return queue


answer = 0
for i in range(m):
    target = targets[i]
    left_count = queue.index(target)
    right_count = len(queue) - queue.index(target)
    # 맨 앞에 빼야하는 원소가 올 때까지
    while target != queue[0]:
        # 오른쪽 이동이 적다면 오른쪽 이동
        if left_count >= right_count:
            for _ in range(right_count):
                queue = moveRight(queue)
                answer += 1
        else:
            for _ in range(left_count):
                queue = moveLeft(queue)
                answer += 1
    queue.popleft()
print(answer)
