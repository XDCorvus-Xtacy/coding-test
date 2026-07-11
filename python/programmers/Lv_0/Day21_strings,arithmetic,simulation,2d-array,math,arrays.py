###################################################

# Day21. strings, arithmetic, simulation,2d-array, math, arrays

###################################################
'''
문제 설명
문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 
대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 
return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ my_string의 길이 ≤ 1,000
1 ≤ my_string 안의 자연수 ≤ 1000
연속된 수는 하나의 숫자로 간주합니다.
000123과 같이 0이 선행하는 경우는 없습니다.
문자열에 자연수가 없는 경우 0을 return 해주세요.
'''
# sol1. 정규식 활용
import re
def solution(my_string):
    number = re.findall(r'\d+', my_string)
    return sum(int(x) for x in number)

# sol2. 정규식 없이
def solution(my_string):
    s = "".join(x if x.isdigit() else ' ' for x in my_string)
    return sum(int(i) for i in s.split())

###################################################
'''
문제 설명
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 
대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 
매설된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 
지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

제한사항
board는 n * n 배열입니다.
1 ≤ n ≤ 100
지뢰는 1로 표시되어 있습니다.
board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
'''
def solution(board):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 0), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    danger = set()
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n:
                        danger.add((nr,nc))
    return n * n - len(danger)

###################################################
'''
문제 설명
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 
함수를 완성해주세요.

제한사항
sides의 원소는 자연수입니다.
sides의 길이는 2입니다.
1 ≤ sides의 원소 ≤ 1,000
'''
def solution(sides):
    return len(range(max(sides)-min(sides)+1, sum(sides)))

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

def solution(sides):
    return 2 * min(sides) - 1

###################################################
'''
문제 설명
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 
언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 
dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 
사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 
return하도록 solution 함수를 완성해주세요.

제한사항
spell과 dic의 원소는 알파벳 소문자로만 이루어져있습니다.
2 ≤ spell의 크기 ≤ 10
spell의 원소의 길이는 1입니다.
1 ≤ dic의 크기 ≤ 10
1 ≤ dic의 원소의 길이 ≤ 10
spell의 원소를 모두 사용해 단어를 만들어야 합니다.
spell의 원소를 모두 사용해 만들 수 있는 단어는 dic에 두 개 이상 존재하지 않습니다.
dic과 spell 모두 중복된 원소를 갖지 않습니다.
'''
def solution(spell, dic):
    spell_set = set(spell)           # spell을 set으로
    for word in dic:                 # dic의 각 단어를
        if set(word) == spell_set:   # set으로 만들어 비교
            return 1                 # 같은 게 있으면 1
    return 2                         # 끝까지 없으면 2

###################################################