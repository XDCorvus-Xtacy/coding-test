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