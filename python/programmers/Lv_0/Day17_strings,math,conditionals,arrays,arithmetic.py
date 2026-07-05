###################################################

# Day17. strings, math, conditionals, arrays, arithmetic

###################################################
'''
문제 설명
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 
k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 
-1을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 < num < 1,000,000
0 ≤ k < 10
num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.

'''
def solution(num, k):
    idx = 0
    str_num = str(num)
    str_k = str(k)
    while idx < len(str_num):
        idx += 1
        if str_num[idx-1] == str_k:
            return idx
    return -1

def solution(num, k):
    for i, digit in enumerate(str(num)):
        if digit == str(k):
            return i + 1      # 자리수는 1부터니까 +1
    return -1

def solution(num, k):
    idx = str(num).find(str(k))
    return idx + 1 if idx != -1 else -1

###################################################
'''
문제 설명
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, 
numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 
solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 10,000
1 ≤ numlist의 크기 ≤ 100
1 ≤ numlist의 원소 ≤ 100,000
'''
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n == 0:
            answer.append(i)
    return answer

def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

###################################################
'''
문제 설명
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 
return하도록 solution 함수를 완성해주세요

제한사항
0 ≤ n ≤ 1,000,000
'''
def solution(n):
    return sum(int(i) for i in str(n))

###################################################
