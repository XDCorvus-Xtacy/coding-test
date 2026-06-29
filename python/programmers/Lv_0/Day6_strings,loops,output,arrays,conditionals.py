###################################################

# Day6. strings, loops, output, arrays, conditionals

###################################################
'''
문제 설명
문자열 my_string이 매개변수로 주어집니다. 
my_string을 거꾸로 뒤집은 문자열을 return하도록 
solution 함수를 완성해주세요.
'''
def solution(my_string):
    return my_string[::-1]

###################################################
'''
"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 
삼각형을 그리려고합니다. 정수 n 이 주어지면 높이와 너비가 n 인 
직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
'''
n = int(input())

for i in range(n):
    print('*'*(i+1))

###################################################
'''
문제 설명
정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 
짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를
완성해보세요.
'''
def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

###################################################
'''
문제 설명
문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 
들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 
함수를 완성해보세요.

제한사항
2 ≤ my_string 길이 ≤ 5
2 ≤ n ≤ 10
"my_string"은 영어 대소문자로 이루어져 있습니다.
'''
# += 는 매번 새로 복사함. 
# 즉 기존의 문자열에 더해지는 것이 아닌 아예 새로 만들어짐
# 그러나 join()은 list를 한번에 합침.
def solution(my_string, n):
    return "".join(i * n for i in my_string)

###################################################