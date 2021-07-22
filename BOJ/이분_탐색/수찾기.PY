# 정수 배열 중에서 X라는 정수의 존재 유무를 찾아내는 문제
# https://www.acmicpc.net/problem/1920
# 이분 탐색의 시간 복잡도 O(log(n))
from sys import stdin
read = stdin.readline
n = int(read())
numbers = list(map(int, read().split()))
# 이분 탐색을 하기 위해서 표본이 되는 배열을 정렬하였습니다.
numbers.sort()

m = int(read())
comp_list = list(map(int, read().split()))


def BinarySearch(numbers, num, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if num == numbers[mid]:
        return True
    elif num < numbers[mid]:
        return BinarySearch(numbers, num, start, mid - 1)
    else:
        return BinarySearch(numbers, num, mid + 1, end)


for num in comp_list:
    if BinarySearch(numbers, num, 0, n-1):
        print(1)
    else:
        print(0)
