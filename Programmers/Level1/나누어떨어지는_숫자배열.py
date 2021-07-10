# 주어진 숫자로 나누어 떨어지면 배열에 추가하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12910

# 점점 파이썬의 한 줄 풀이에 적응해가고 있습니다.
# 이 문제에서 알게된 점은 빈 리스트일 경우 False를 반환하는 점입니다. 이를 이용해서 빈 배열일 경우 -1을 추가하였습니다.
def solution(arr, divisor):
    answer = [n for n in arr if n % divisor == 0]
    answer.sort() if answer else answer.append(-1)
    return answer