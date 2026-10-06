# 계단 1

'''
각 원소가 자기 "부모"를 가리키는 리스트 parent가 주어집니다.
자기 자신을 가리키는 원소가 그 무리의 대표(루트)입니다.

find(parent, x): x의 대표를 반환하세요.

parent = [0, 0, 1, 3, 3, 4]
인덱스    0  1  2  3  4  5

예) find(parent, 2)  →  0
    find(parent, 5)  →  3
    find(parent, 3)  →  3
'''
def find(parent, x):
    if parent[x] == x:
        return x
    
    return find(parent, parent[x])



# 계단 2
'''
parent = [0, 0, 1, 3, 3, 4]
인덱스    0  1  2  3  4  5

  0        3
  ↑        ↑
  1        4
  ↑        ↑
  2        5

무리 A = {0, 1, 2}   대표 0
무리 B = {3, 4, 5}   대표 3
'''
def union(parent, a, b):
    president = find(parent, a)
    move = find(parent, b)
    parent[move] = president