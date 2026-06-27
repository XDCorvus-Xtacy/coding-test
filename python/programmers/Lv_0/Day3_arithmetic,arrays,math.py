###################################################

# Day3. arithmetic, arrays, math

###################################################
'''
문제 설명
정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 
나머지를 return 하도록 solution 함수를 완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
'''
def solution(num1, num2):
    return num1%num2

###################################################
'''
문제 설명
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 
중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 
중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때,
중앙값을 return 하도록 solution 함수를 완성해보세요.

제한사항
array의 길이는 홀수입니다.
0 < array의 길이 < 100
-1,000 < array의 원소 < 1,000
'''
def solution(array):
    array.sort()
    return array[len(array)//2]

###################################################
'''
문제 설명
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 
solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

제한사항
0 < array의 길이 < 100
0 ≤ array의 원소 < 1000
'''
def solution(array):
    dic = {}
    for i in array:
        dic[i] = dic.get(i,0) + 1
    
    max_count = max(dic.values())
    result = [k for k, v in dic.items() if v == max_count]
    
    if len(result) == 1:
        return result[0]
    else:
        return -1

###################################################
'''
문제 설명
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 
배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100
'''
def solution(n):
    return [i for i in range(1, n+1, 2)]
