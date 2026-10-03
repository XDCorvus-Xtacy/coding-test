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