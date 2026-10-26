# 계단 1: 두 집합 합치기
'''
combine(A, B)

집합 A의 원소 a와 집합 B의 원소 b로 만들 수 있는
a + b,  a - b,  a * b,  a // b (b가 0이 아닐 때만)
를 전부 담은 집합을 반환하세요.

예) combine({5}, {5})       →  {10, 0, 25, 1}
    combine({10, 25}, {5})   →  {15, 5, 50, 2, 30, 20, 125}
    combine({5}, {0})        →  {5, 0}          ← 0으로 나누기는 건너뜀
'''
def combine(a, b):
    result = set()
    for i in a:
        for j in b:
            result.update({i+j, i-j, i*j, j-i})
            if i != 0:
                result.add(j//i)
            if j != 0:
                result.add(i//j)
    return result



# 계단 2: dp[3]까지 직접 만들기
n = 4   # 5를 4개까지 쓰는 dp 작성
dp = [set() for _ in range(n+1)]
dp[1] = {5}
dp[2] = {55} | combine(dp[1], dp[1])
dp[3] = {555} | combine(dp[2], dp[1])
dp[4] = {5555} | combine(dp[3], dp[1]) | combine(dp[2], dp[2])



# 계단 3: 계단 2를 반복문으로 만들기
n = 4   # 5를 4개까지 쓰는 dp 작성
N = input()
dp = [set() for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = {int(N*i)}
    for j in range(1, i//2 + 1):
        dp[i] = dp[i] | combine(dp[i-j], dp[j])
    
    print(len(dp[i]))   # 1 5 18 66
