# 2개의 배열에 들어있는 10진수를 각 2진수로 변환한 뒤 or 연산을 해서 1과 0에 맞는 문자를 배치하는 문제
# 한 번 더 파이썬 라이브러리의 편리함과 경이로움을 느낄 수 있었던 시간이었다..
# https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1,arr2):
        # 2진수 변환을 위해 divmod 함수를 사용해서 나머지 연산을 하려고 했는데 계산해주는 bin 함수가 있었다...
        # bin 함수는 앞 2자리가 진수를 표현한다. 2번부터 인덱싱하였다.
        num = str(bin(a1|a2)[2:])
        if len(num) < n:
            num = '0' * (n-len(num)) + num
        # for문을 돌면서 비교해서 변환하려고 했는데 마침 파이썬에 replace라는 좋은 함수가 있었다..
        num = num.replace('1','#')
        num = num.replace('0',' ')
        answer.append(num)
                
    return answer

# 파이썬 bin, replace 라이브러리 활용 전 풀이했던 코드
# binary 연산은 divmod로 나머지를 구하고 자리수가 부족한 경우 0을 추가한 후 문자열을 뒤집어서 구했다.
# 그 후에도 문자 변환을 위해 for 루프를 사용했는데 라이브러리를 사용하였더니
# 위에 코드처럼 간결하며 실행 시간도 최대 0.3초 줄어든 코드를 짤 수 있었다. 오마이갓 파이썬 너무 신기하다!

# def mod(q, n):
#     s = ''
#     while q >= 1:
#             q, rest = divmod(q,2)
#             s += str(rest)
#     if len(s) < n:
#         s += '0' * (n-len(s))
#     return s[::-1]


# def solution(n, arr1, arr2):
#     answer = []
    
#     for a1, a2 in zip(arr1,arr2):    
#         s1 = mod(a1, n)
#         print(s1)
#         s2 = mod(a2, n)
        
#         s3 = ''
#         for i in range(len(s1)):
#             if s1[i] == '1' or s2[i] == '1':
#                 s3 += '#'
#             else:
#                 s3 += ' '
        
#         answer.append(s3)
                
#     return answer