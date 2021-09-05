# https://programmers.co.kr/learn/courses/30/lessons/67257
"""
문제
해커톤 대회에 참가하는 모든 참가자들에게는 숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식이 전달되며, 참가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하는 것입니다.
단, 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 합니다. 즉, + > - > * 또는 - > * > + 등과 같이 연산자 우선순위를 정의할 수 있으나 +,* > - 또는 * > +,-처럼 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없습니다. 수식에 포함된 연산자가 2개라면 정의할 수 있는 연산자 우선순위 조합은 2! = 2가지이며, 연산자가 3개라면 3! = 6가지 조합이 가능합니다.
참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 우승 시 받을 수 있는 가장 큰 상금 금액을 return 하도록 solution 함수를 완성해주세요.

제한사항
expression은 길이가 3 이상 100 이하인 문자열입니다.
expression은 공백문자, 괄호문자 없이 오로지 숫자와 3가지의 연산자(+, -, *) 만으로 이루어진 올바른 중위표기법(연산의 두 대상 사이에 연산기호를 사용하는 방식)으로 표현된 연산식입니다. 잘못된 연산식은 입력으로 주어지지 않습니다.
 > 즉, "402+-561*"처럼 잘못된 수식은 올바른 중위표기법이 아니므로 주어지지 않습니다.
expression의 피연산자(operand)는 0 이상 999 이하의 숫자입니다.
 > 즉, "100-2145*458+12"처럼 999를 초과하는 피연산자가 포함된 수식은 입력으로 주어지지 않습니다.
 > "-56+100"처럼 피연산자가 음수인 수식도 입력으로 주어지지 않습니다.
expression은 적어도 1개 이상의 연산자를 포함하고 있습니다.
연산자 우선순위를 어떻게 적용하더라도, expression의 중간 계산값과 최종 결괏값은 절댓값이 263 - 1 이하가 되도록 입력이 주어집니다.
같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높습니다.

입출력
expression	result
"100-200*300-500+20"	60420
"50*6-3*2"	300
"""
from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(exp, op):
    exp_list = []
    tmp = ""
    for s in exp:
        if s.isdigit():
            tmp += s
        else:
            exp_list.append(tmp)
            exp_list.append(s)
            tmp = ""
    exp_list.append(tmp)

    for each_op in op:
        stack = []
        while len(exp_list) != 0:
            tmp = exp_list.pop(0)
            if tmp == each_op:
                # 100 + 200 * 300 의 경우에 *가 우선순위가 높을 때,
                # stack = [100, 200] each_op = * exp_list = [300]이므로
                # stack의 마지막 값과 list의 첫 번째 값을 연산한다.
                stack.append(operation(stack.pop(), exp_list.pop(0), each_op))
            else:
                stack.append(tmp)
        exp_list = stack
    return abs(int(exp_list[0]))


def solution(expression):
    result = []
    operations = list(permutations(['+', '-', '*'], 3))

    for op in operations:
        result.append(calculate(expression, op))

    return max(result)
