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



# 계단 3
'''
사슬 모양이 되면 find가 매번 끝까지 걸어감
parent = [0, 0, 1, 2, 3, 4]  →  find(5)를 두 번 하면 5칸 + 5칸

첫 find에서 알아낸 "지나온 칸들의 대표 = 0"을 parent에 남겨두면
두 번째 find는 1칸으로 끝남

트리 모양이 바뀌어도 괜찮은 이유:
  유니온-파인드가 답하는 건 "같은 무리인가"뿐 (find 결과가 같은가)
  화살표는 대표에게 가는 이정표일 뿐, BST처럼 모양 자체가 정보가 아님
'''
def find_compress(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find_compress(parent, parent[x])

    return parent[x]