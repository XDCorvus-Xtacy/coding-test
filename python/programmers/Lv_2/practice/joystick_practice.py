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