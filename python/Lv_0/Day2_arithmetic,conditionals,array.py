###################################################

# Day2. arithmetic, conditionals, array

###################################################
'''
문제 설명
정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 
값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 
완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
'''
def solution(num1, num2):
    return int(num1/num2*1000)

###################################################
'''
문제 설명
정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 
다르면 -1을 retrun하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ num1 ≤ 10,000
0 ≤ num2 ≤ 10,000
'''
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

###################################################
'''
문제 설명
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 
분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 
담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 <numer1, denom1, numer2, denom2 < 1,000
'''
import math

def solution(numer1, denom1, numer2, denom2):
    
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    div = math.gcd(numer, denom)
    
    answer = [numer//div, denom//div]

    return answer

###################################################
'''
문제 설명
정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 
두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
-10,000 ≤ numbers의 원소 ≤ 10,000
1 ≤ numbers의 길이 ≤ 1,000
'''
# sol 1 - lambda fnction
def solution(numbers):
    answer = list(map(lambda x:x*2, numbers))
    return answer

# sol 2 - list comprehension
def solution(numbers):
    return [x*2 for x in numbers]

# sol 3 - using for
def solution(numbers):
    answer = []
    for x in numbers:
        answer.append(x*2)
    return answer