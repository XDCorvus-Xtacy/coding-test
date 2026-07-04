###################################################

# Day16. strings, math, arrays, conditionals

###################################################
'''
문제 설명
머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 
할머니가 보시기 편하도록 글자 한 자 한 자를 가로 
2cm 크기로 적으려고 하며, 편지를 가로로만 적을 때, 
축하 문구 message를 적기 위해 필요한 편지지의 최소 
가로길이를 return 하도록 solution 함수를 완성해주세요.

제한사항
공백도 하나의 문자로 취급합니다.
1 ≤ message의 길이 ≤ 50
편지지의 여백은 생각하지 않습니다.
message는 영문 알파벳 대소문자, ‘!’, ‘~’ 또는 공백으로만 이루어져 있습니다.
'''
def solution(message):
    return len(message)*2

###################################################
'''
문제 설명
정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 
그 수의 인덱스를 담은 배열을 return 하도록 solution 
함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
0 ≤ array 원소 ≤ 1,000
array에 중복된 숫자는 없습니다.
'''
# O(n)
def solution(array):
    max_val = 0
    max_idx = 0
    for k, v in enumerate(array):
        if max_val < v:
            max_val = v
            max_idx = k
    return [max_val, max_idx]

# O(2n)
def solution(array):
    max_val = max(array)
    return [max_val, array.index(max_val)]

###################################################
'''
문제 설명
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 
return 하는 solution 함수를 완성해주세요.

제한사항
연산자는 +, -만 존재합니다.
문자열의 시작과 끝에는 공백이 없습니다.
0으로 시작하는 숫자는 주어지지 않습니다.
잘못된 수식은 주어지지 않습니다.
5 ≤ my_string의 길이 ≤ 100
my_string을 계산한 결과값은 1 이상 100,000 이하입니다.
my_string의 중간 계산 값은 -100,000 이상 100,000 이하입니다.
계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.
my_string에는 연산자가 적어도 하나 포함되어 있습니다.
return type 은 정수형입니다.
my_string의 숫자와 연산자는 공백 하나로 구분되어 있습니다.
'''
def solution(my_string):
    tokens = my_string.split(" ")
    answer = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = int(tokens[i+1])
        if op == '+':
            answer += num
        else:
            answer -= num
    return answer

###################################################
'''
문제 설명
두 배열이 얼마나 유사한지 확인해보려고 합니다. 
문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 
return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ s1, s2의 길이 ≤ 100
1 ≤ s1, s2의 원소의 길이 ≤ 10
s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
s1과 s2는 각각 중복된 원소를 갖지 않습니다.
'''
def solution(s1, s2):
    result = 0
    for i in s1:
        for j in s2:
            if i == j:
                result += 1
    return result

def solution(s1, s2):
    result = 0
    s2_set = set(s2)
    for i in s1:
        if i in s2_set:
            result += 1
    return result

def solution(s1, s2):
    return len(set(s1) & set(s2))

###################################################
