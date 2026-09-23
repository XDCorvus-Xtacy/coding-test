'''
정수 n이 주어질 때, 1부터 n까지의 수 중 소수를 모두 찾아 리스트로 반환하세요.
(소수: 1과 자기 자신 외의 약수가 없는 수. 1은 소수가 아님)

예) n = 30
→ [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

목표 복잡도: O(n log log n)
'''
def sieve(n):
    answer = []
    prime = [0, 0] + [1]*(n-1)
    for i in range(2, n+1):
        if prime[i] == 1:
            answer.append(i)
            for j in range(i*i, n+1, i):
                prime[j] = 0
    return answer