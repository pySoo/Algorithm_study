# 주어진 숫자에서 k개의 문자를 제거했을 때 가장 큰 수를 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = ''
    stack = [number[0]]
    
    for n in number[1:]:
        # 스택의 마지막 원소보다 새로운 값이 큰 경우
        while stack and stack[-1] < n:
            # 뺄 수 있는 개수가 남았다면 값을 제거합니다.
            if k > 0:
                k -= 1
                stack.pop()
            else:
                break
        # 새로운 값보다 작은 값들을 모두 빼고 새로운 값을 넣습니다.
        stack.append(n)
    
    # 이 부분 때문에 통과를 못 했는데, 최적의 수를 구했음에도 빼야하는 갯수가 남았다면
    # 뒤에서 k개 만큼 자르도록 합니다.
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)