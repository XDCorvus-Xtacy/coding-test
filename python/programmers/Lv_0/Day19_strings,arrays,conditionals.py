###################################################

# Day19. strings, arrays, conditionals

###################################################
'''
문제 설명
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 
return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
0 ≤ array의 원소 ≤ 100,000
'''
def solution(array):
    return "".join(map(str, array)).count("7")

###################################################
'''
문제 설명
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 
잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ my_str의 길이 ≤ 100
1 ≤ n ≤ my_str의 길이
my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.
'''
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

###################################################
'''
문제 설명
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 n이 몇 개 있는 지를 return 하도록 solution 
함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
0 ≤ array의 원소 ≤ 1,000
0 ≤ n ≤ 1,000
'''
def solution(array, n):
    cnt = 0
    for i in array:
        if i == n:
            cnt += 1
    return cnt

def solution(array, n):
    return array.count(n)

###################################################
'''
문제 설명
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 
궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 
머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 
사람 수를 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
1 ≤ height ≤ 200
1 ≤ array의 원소 ≤ 200

'''
def solution(array, height):
    return sum(1 for x in array if height < x)

###################################################
