'''
문제 설명
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 
return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
'''
def solution(n):
    arr = []
    while n > 0:
        arr.append(str(n%3))
        n //= 3
        
    answer = "".join(arr)
    return int(answer, 3)

# 매개변수를 함수 안에서 건드릴 때:
# - 불변 객체 (int, str, tuple) → 재바인딩만 일어남. 호출자 안전
# - 가변 객체 (list, dict, set)  → 객체 직접 수정. 호출자 원본 변형 