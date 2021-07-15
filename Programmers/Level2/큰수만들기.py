# 주어진 숫자에서 k개의 문자를 제거했을 때 가장 큰 수를 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = ''
    stack = [number[0]]
    
    for n in number[1:]:
        while stack and stack[-1] < n:
            if k > 0:
                k -= 1
                stack.pop()
            else:
                break
        stack.append(n)
    
    if k>0:
        stack = stack[:-k]
    return ''.join(stack)