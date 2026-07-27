'''
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, 
solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
'''
# 소수 찾기 (Programmers Lv.1)
# 핵심: 에라토스테네스의 체 — 인덱스가 곧 숫자
# 최적화 3단계: 바깥 √n까지 / 안쪽 i*i부터 / 파이썬 루프 → 슬라이스 대입

# sol1. for 루프 마킹 (0.173초 @ n=100만)
# sol2. 슬라이스 대입, 길이=슬라이스 복사 (0.035초) ← 실질적 도약
# sol3. 슬라이스 대입, 길이=range 계산 (0.024초) ← 복사 제거

#sol1. using for
def solution(n):
    prime = [0, 0] + [1]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if prime[i] == 1:
            for j in range(i*i,n+1,i):
                prime[j] = 0
        else:
            pass
    return prime.count(1)

#sol2. using slice(slicing copy)
def solution(n):
    prime = [0, 0] + [1]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if prime[i] == 1:
            prime[i*i::i] = [0] * len(prime[i*i::i])
            
    return prime.count(1)

#sol3. using slice(range)
def solution(n):
    prime = [0, 0] + [1]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if prime[i] == 1:
            prime[i*i::i] = [0] * len(range(i*i, n+1, i))            

    return prime.count(1)
