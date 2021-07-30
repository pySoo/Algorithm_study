# https://www.acmicpc.net/problem/1003
"""
문제
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.
fibonacci(N)을 호출했을 때 0과 1이 각 몇 번 출력되는지 구하시오.
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""
# 재귀 함수로만 풀면 시간 제한이 되기 때문에 DP를 이용해야한다.
zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))


T = int(input())

for _ in range(T):
    fibonacci(int(input()))
