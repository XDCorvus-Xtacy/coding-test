###################################################

# Day14. conditionals, loops, simulation, strings

###################################################
'''
문제 설명
정수 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 
solution 함수를 완성해주세요.

제한사항
1 ≤ array의 길이 ≤ 100
1 ≤ array의 원소 ≤ 100
1 ≤ n ≤ 100
가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
'''
def solution(array, n):
    return min(array, key=lambda x: (abs(x-n), x))

###################################################
'''
문제 설명
머쓱이는 친구들과 369게임을 하고 있습니다. 
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 
숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 
머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 
완성해보세요.

제한사항
1 ≤ order ≤ 1,000,000

'''
def solution(order):
    return sum(1 for i in str(order) if i in "369")

###################################################
'''
문제 설명
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 
사용한다는 것을 알아냈습니다.

암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 
문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ cipher의 길이 ≤ 1,000
1 ≤ code ≤ cipher의 길이
cipher는 소문자와 공백으로만 구성되어 있습니다.
공백도 하나의 문자로 취급합니다.
'''
def solution(cipher, code):
    return cipher[code-1::code]

###################################################
'''
문제 설명
문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 
소문자는 대문자로 변환한 문자열을 return하도록 solution 
함수를 완성해주세요.

제한사항
1 ≤ my_string의 길이 ≤ 1,000
my_string은 영어 대문자와 소문자로만 구성되어 있습니다.
'''
def solution(my_string):
    return my_string.swapcase()

# using ASCII
# 'A'=65, 'a'=97 → 차이 32
# 'A' + 32 = 'a',  'a' - 32 = 'A'
def solution(my_string):
    result = ""
    for c in my_string:
        if c.isupper():
            result += chr(ord(c) + 32)   # 대문자 → 소문자
        else:
            result += chr(ord(c) - 32)   # 소문자 → 대문자
    return result

###################################################
