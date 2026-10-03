"""
조이스틱 재학습 (계단) — 2026-10-03
10/1 docs 이후 이해 단계. 계단 1~2 완료, 계단 3 남음

[계단 1] 되돌기 지점 i, j가 정해졌을 때 좌우 최소 이동
  부품 두 개:
    0 ↔ i  (오른쪽 방향)       = i
    0 ↔ j  (왼쪽, 원형 넘어감)  = n - j
  경로 1. 오른쪽으로만          n - 1
  경로 3. 오른쪽 먼저 되돌기    2i + (n - j)   ← 오른쪽을 왕복
  경로 4. 왼쪽 먼저 되돌기      i + 2(n - j)   ← 왼쪽을 왕복
  → 먼저 가는 쪽은 왕복이라 2배, 나중 쪽은 1배
  예) "BBBAAAB" (i=2, j=6): 6 / 5 / 4
      "BBAAAAB" (i=1, j=6): 6 / 3 / 3

[계단 2] i가 주어졌을 때 j 찾기
  - i + 1 부터 본다 (i 자신을 j로 잡지 않도록)
  - 'A'가 아닌 첫 위치를 반환
  - 끝까지 A면 n 을 반환
      j는 인덱스가 아니라 식에서 "n - j"로만 쓰임
      j = n  →  n - j = 0  →  "왼쪽으로 갈 거리 없음"
      경로 4가 i가 되어 "오른쪽으로 i까지만 가고 끝"이 자연스럽게 계산됨
      -1 이나 n-1 을 반환하면 갈 필요 없는 왼쪽 거리가 더해져 틀림
      예) "BBAAA", i=1 → j=5 일 때 1 (정답) / j=-1 일 때 4 (오답)

[계단 3 — 다음 시간]
  i를 어디로 잡나?
"""


# 계단 1
'''
turn_cost(n, i, j)

i와 j가 주어졌을 때, 경로 3과 경로 4 중 더 짧은 좌우 이동 횟수를 반환

예) turn_cost(7, 2, 6) → 4    ("BBBAAAB")
    turn_cost(7, 1, 6) → 3    ("BBAAAAB")
'''
def turn_cost(n, i, j):
    route_1 = n-1
    route_2 = 2*i + n-j
    route_3 = 2*(n-j) + i
    return min(route_1, route_2, route_3)



# 계단 2
'''
find_j(name, i)

i 다음부터 'A'가 아닌 첫 위치를 반환

name = "BABAAAB"
        0123456

예) find_j(name, 0)  →  2
    find_j(name, 2)  →  6
'''
def find_j(name, i):
    for j in range(i+1, len(name)):
        if name[j] != 'A':
            return j
    return len(name)