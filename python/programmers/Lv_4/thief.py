'''
도둑이 마을을 털려고 합니다. 모든 집은 동그랗게 배치되어 있고,
인접한 두 집을 털면 경보가 울립니다.
각 집에 있는 돈이 담긴 배열 money가 주어질 때,
도둑이 훔칠 수 있는 돈의 최댓값을 return 하세요.

[제한사항]
- 집은 3개 이상 1,000,000개 이하
- money의 각 원소는 0 이상 1,000 이하인 정수

[입출력 예]
money           return
[1, 2, 3, 1]    4
'''
def solution(money):
    answer = 0
    return answer


# 계단 1: 집이 일렬일 때 (첫 집과 마지막 집은 이웃이 아님)
def solve_line(money):
    length = len(money)
    dp = [0]*length
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[0] + money[2]

    for i in range(3, length):
        dp[i] = max(dp[i-2] + money[i], dp[i-3] + money[i])

    return max(dp[-1], dp[-2])


print(solve_line([1, 2, 3, 1]))          # 기대값: 4
print(solve_line([2, 7, 9, 3, 1]))       # 기대값: 12
print(solve_line([5, 1, 1, 5]))          # 기대값: 10 (i-3에서 오는 경우)
print(solve_line([1, 2, 3]))             # 기대값: 4  (가장 짧은 입력)
print(solve_line([1, 100, 1, 1, 100]))   # 기대값: 200