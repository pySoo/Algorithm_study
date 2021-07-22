# 중복 숫자가 있는 배열 중에서 내가 가진 카드 숫자가 몇 개 있는지 구하는 문제
# https://www.acmicpc.net/problem/10816
# 존재 여부는 이분 탐색으로 구했지만, 중복 숫자들이 있기 때문에 총 개수를 어떻게 구해야할 지 고민이었습니다.
# 처음에 dictionary를 이용하여 숫자별 개수를 저장해서 해결한 풀이를 참고하였습니다.
from sys import stdin
read = stdin.readline
n = int(read())
numbers = list(map(int, read().split()))
m = int(read())
card = list(map(int, read().split()))
dic = {}

# 미리 numbers의 숫자별 개수를 저장해놓습니다.
for c in numbers:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1


def binary(numbers, num, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if numbers[mid] == num:
        return True
    elif numbers[mid] > num:
        return binary(numbers, num, start, mid-1)
    else:
        return binary(numbers, num, mid+1, end)


numbers.sort()
# 만약 찾는 숫자가 배열에 있다면 총 개수를 저장한 dic을 이용해서 총 개수를 구합니다.
for num in card:
    if binary(numbers, num, 0, n-1):
        print(dic[num], end=" ")
    else:
        print(0, end=" ")
