###################################################

# Day12. strings, sorting, arithmetic, math

###################################################
'''
문제 설명
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 
return하도록 solution 함수를 완성해주세요.

제한사항
my_string은 소문자와 공백으로 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
'''
# replace 사용
def solution(my_string):
    for word in "aeiou":
        my_string = my_string.replace(word, "")
    return my_string

# 튜플, join 사용 : 시간복잡도 O(1)
def solution(my_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return "".join(c for c in my_string if c not in vowels)

# 정규표현식
import re
def solution(my_string):
    return re.sub("[aeiou]", "", my_string)

###################################################
'''
문제 설명
문자열 my_string이 매개변수로 주어질 때, my_string 안에 
있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 
solution 함수를 작성해보세요.

제한사항
1 ≤ my_string의 길이 ≤ 100
my_string에는 숫자가 한 개 이상 포함되어 있습니다.
my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 
있습니다. - - -
'''
import re

def solution(my_string):
    answer = []
    num_list = re.sub("[a-zA-Z]", "", my_string)
    for i in num_list:
        answer.append(int(i))
    return sorted(answer)

def solution(my_string):
    return sorted(int(c) for c in my_string if c.isdigit())

###################################################
'''
문제 설명
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 
n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 
함수를 완성해주세요.

제한사항
2 ≤ n ≤ 10,000
'''
# sol1. 약수 구하고 그 중 소수인 것만 추리기
def get_divisors(n):
    divisors = []
    # n의 제곱근까지만 탐색하여 성능 최적화
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            # i가 제곱근이 아닌 경우, 짝이 되는 약수 추가
            if i != n // i:
                divisors.append(n // i)
                
    return sorted(divisors)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(n):
    return [d for d in get_divisors(n) if is_prime(d)]


# sol2. 소인수 직접 구하기
def solution(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:          # d가 소인수
            answer.append(d)
            while n % d == 0:   # d로 안 나눠질 때까지 나눔
                n //= d
        d += 1
    if n > 1:                   # 남은 게 있으면 그것도 소인수
        answer.append(n)
    return answer
    
###################################################
