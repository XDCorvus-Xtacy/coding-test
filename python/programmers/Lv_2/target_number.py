'''
문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 
타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 
다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 
작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
'''
def solution(numbers, target):
    length = len(numbers)
    def dfs(index, total):
        if index == length:
            return 1 if total == target else 0
        return dfs(index+1, total+numbers[index]) + dfs(index+1, total-numbers[index])
    answer = dfs(0, 0)
    return answer


# 타겟 넘버 (Programmers Lv.2, DFS/BFS)
# 상태: 구조 이해 완료, 자력 설계는 미완 → 재현 대상
#
# [재귀 설계 3질문]
# Q1. 이 함수는 뭘 돌려주는가?
#     → index번째부터 끝까지 처리해서 target을 만드는 "방법의 개수"
# Q2. 언제 즉시 답할 수 있는가? (종료 조건)
#     → 숫자를 다 썼을 때. total == target이면 1, 아니면 0
# Q3. 지금 하나만 처리하고 나머지는 자신에게 맡기면?
#     → 지금 숫자는 + 또는 -. 두 갈래 결과를 "더한다"
#
# [핵심]
# - 호출 1개 = 일직선 / 호출 2개 = 트리로 갈라짐
# - 자식이 "내 아래에 정답이 몇 개"를 부모에게 올려보냄
# - C++ 트리 순회와 동일 구조:
#     count(node->left) + count(node->right)