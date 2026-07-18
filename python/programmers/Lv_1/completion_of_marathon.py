'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 
작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

# Counter 활용.(내부 구현은 위와 동일함)
from collections import Counter
def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result)[0]  #Counter 객체는 list로 감싸면 자동으로 key만!

'''
Counter 클래스 (from collections import Counter)

- 하는 일: 원소 개수 세기. 내부적으로 아래와 동일
    d = {}
    for name in namelist:
        d[name] = d.get(name, 0) + 1

- 반환: Counter 객체 (dict를 상속 → dict처럼 쓸 수 있음)
- key만 꺼내기: list(counter) → key 리스트

- 지원 연산: +, -, &(min), |(max)
    · +  : 카운트 합침
    · -  : 카운트 뺌 → 결과 0 이하 key 자동 삭제
    · 곱셈/나눗셈은 없음

- 음수를 살리고 싶다면 (연산자 대신 메서드):
    a = Counter({'x': 1})
    b = Counter({'x': 3})
    a - b           # {}         (음수 버림, 새 객체 반환)
    a.subtract(b)   # {'x': -2}  (음수 유지, 원본 수정)
'''