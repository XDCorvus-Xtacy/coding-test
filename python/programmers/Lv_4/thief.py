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
# 계단 1: 집이 일렬일 때 (첫 집과 마지막 집은 이웃이 아님)
def solve_line(dp):
    length = len(dp)

    for i in range(3, length):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])

    return max(dp[-1], dp[-2])



# 계단 2: 원형 — 두 경우로 나눠 solve_line 재사용
def solution(money):
    if len(money) == 3:
        return max(money)

    def solve_line(dp):
        length = len(dp)

        for i in range(3, length):
            dp[i] = max(dp[i-2] + money[i], dp[i-1])

        return max(dp[-1], dp[-2])


    length = len(money)
    dp_one = [0]*(length-1)     # money[0]을 포함한 경우
    dp_two = [0]*length         # money[0]을 포함하지 않은 경우

    dp_one[0] = money[0]
    dp_one[1] = dp_one[0]
    dp_one[2] = money[0] + money[2]

    one_return = solve_line(dp_one)
    
    dp_two[0] = 0
    dp_two[1] = money[1]
    dp_two[2] = max(money[1], money[2])

    two_return = solve_line(dp_two)

    return max(one_return, two_return)

print(solution([1, 2, 3, 1]))          # 기대값: 4  (공식 예시)
print(solution([1, 2, 3]))             # 기대값: 3  (집 3개: 하나만 털 수 있음)
print(solution([5, 1, 1, 5]))          # 기대값: 6  (0번과 3번은 이웃)
print(solution([1, 100, 1, 1, 100]))   # 기대값: 200  (1번 + 4번, 둘은 이웃이 아님)
print(solution([0, 0, 0]))             # 기대값: 0