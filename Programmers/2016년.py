# 윤년인 2016년도의 요일을 계산하는 문제
# 날짜 계산 문제는 자주 나오는 유형이므로 유의해야겠다. 적절한 풀이가 생각나지 않아서 다른 분의 코드를 참고하였다.
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    # 1월1일이 금요일이므로 인덱스 1이 금요일로 나오게 설정
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED'] 
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    
    # month 배열의 (a-1)월까지 더한수에서 나머지 일수를 더하여 계산 -> 파이썬 슬라이싱 이용
    # 3월이면 2월까지의 날짜를 다 더함
    date = (sum(month[:a-1]) + b) % 7
    return day[date]