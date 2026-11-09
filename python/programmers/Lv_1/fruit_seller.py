'''
사과는 상태에 따라 1점부터 k점까지 점수가 매겨집니다 (k점이 최상품).
한 상자에 사과를 m개씩 담아 팔고, 상자 가격은 (상자 안 가장 낮은 점수) × m 입니다.
상자 단위로만 팔고, 남는 사과는 버립니다.
k, m, 사과 점수 score가 주어질 때, 얻을 수 있는 최대 이익을 return 하세요.

[제한사항]
- 3 ≤ k ≤ 9
- 3 ≤ m ≤ 10
- 7 ≤ score의 길이 ≤ 1,000,000
- 1 ≤ score[i] ≤ k

[입출력 예]
k    m    score                                  result
3    4    [1, 2, 3, 1, 2, 3, 1]                  8
4    3    [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]   33
'''
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    for i in range(m-1, len(score), m):
        answer += score[i]*m
    
    return answer