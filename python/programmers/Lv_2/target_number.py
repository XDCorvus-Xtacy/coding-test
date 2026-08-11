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

def solution(numbers, target):
    def dfs(index, total):
        if index == len(numbers):
            return 1 if total == target else 0
        return dfs(index+1, total+numbers[index]) + dfs(index+1, total-numbers[index])
    return dfs(0, 0)