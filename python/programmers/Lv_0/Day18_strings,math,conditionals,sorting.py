###################################################

# Day18. strings, math, conditionals, sorting

###################################################
'''
문제 설명
문자열 str1, str2가 매개변수로 주어집니다. 
str1 안에 str2가 있다면 1을 없다면 2를 return하도록 
solution 함수를 완성해주세요.

제한사항
1 ≤ str1의 길이 ≤ 100
1 ≤ str2의 길이 ≤ 100
문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.
'''
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2

###################################################
'''
문제 설명
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 
return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 1,000,000
'''
def solution(n):
    if int((n**0.5))**2 == n:
        return 1
    else:
        return 2

import math
def solution(n):
    root = math.isqrt(n)      # 정수 제곱근 (내림), 오차 없음
    return 1 if root * root == n else 2

###################################################
'''
문제 설명
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 
t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 10
1 ≤ t ≤ 15

'''
def solution(n, t):
    return n*(2**t)

###################################################
'''
문제 설명
영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, 
my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 
return 하도록 solution 함수를 완성해보세요.

제한사항
0 < my_string 길이 < 100
'''
def solution(my_string):
    return "".join(sorted(my_string.lower()))

###################################################
