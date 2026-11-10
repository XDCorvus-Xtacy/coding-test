'''
숫자 N과 사칙연산만 사용해서 number를 표현할 때, N 사용 횟수의 최솟값을 return 하세요.
예) 12 = 5 + 5 + (5 / 5) + (5 / 5)  → 6번
    12 = 55 / 5 + 5 / 5             → 5번
    12 = (55 + 5) / 5               → 4번

[제한사항]
- N은 1 이상 9 이하
- number는 1 이상 32,000 이하
- 수식에는 괄호와 사칙연산만 가능하며, 나누기 연산에서 나머지는 무시
- 최솟값이 8보다 크면 -1을 return

[입출력 예]
N    number    return
5    12        4
2    11        3
'''
def solution(N, number):
    def combine(a, b):
        result = set()
        for i in a:
            for j in b:
                result.update({i+j, i-j, j-i, i*j})
                if i != 0:
                    result.add(j//i)
                if j != 0:
                    result.add(i//j)

        return result

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i//2 + 1):
            dp[i].update(combine(dp[i-j], dp[j]))

        if number in dp[i]:
            return i

    return -1


print(solution(5, 12))      # 기대값: 4  (공식 예시)
print(solution(2, 11))      # 기대값: 3  (공식 예시)
print(solution(5, 5))       # 기대값: 1  (N 하나)
print(solution(5, 555))     # 기대값: 3  (이어붙인 수만으로)
print(solution(5, 110))     # 기대값: 4  (55 + 55)
print(solution(9, 1))       # 기대값: 2  (9 / 9)
print(solution(1, 70))      # 기대값: -1 (8번 넘게 필요)
print(solution(5, 31168))   # 기대값: -1 (8번 넘게 필요)