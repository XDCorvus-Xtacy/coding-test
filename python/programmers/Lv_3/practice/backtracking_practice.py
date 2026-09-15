##########################################
# 계단 1
##########################################
'''
리스트 arr이 주어질 때, 모든 순열(permutation)을 만들어 반환하세요.

예) arr = [1, 2, 3]
→ [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]   (6가지)
'''
def permutation_self(arr):
    def dfs(path, remain):
        if not remain:
            result.append(path[:])
            return
        for i in range(len(remain)):
            picked = remain.pop(i)
            path.append(picked)

            dfs(path, remain)

            path.pop()
            remain.insert(i, picked)
    result = []
    dfs([], remain[:])
    return result



##########################################
# 계단 2
##########################################
'''
리스트 arr과 target이 주어집니다.
arr에서 일부를 골라 합이 정확히 target이 되는 조합이 있으면 그 조합을,
없으면 None을 반환하세요.

예) arr = [3, 34, 4, 12, 5, 2], target = 9  → [3, 4, 2]  (또는 [4, 5])
    arr = [3, 34, 4, 12, 5, 2], target = 30 → None
'''
def solution(arr, target):
    def dfs(path, remain, total):
        if total == target:
            return True
        elif not remain or total > target:
            return False

        for i in range(len(remain)):
            picked = remain.pop(i)
            path.append(picked)

            if dfs(path, remain, total + picked):
                return True
            path.pop()
            remain.insert(i, picked)
        return False
        
    path = []
    if dfs(path, arr[:], 0):
        return path
    return None



##########################################
# 계단 3
##########################################
'''
간선 목록이 주어집니다. 시작점에서 출발해 모든 간선을 한 번씩 사용하는
경로가 있으면 True, 없으면 False를 반환하세요.

예) edges = [["A","B"], ["B","C"], ["C","A"]], start = "A"
    → True   (A→B→C→A, 간선 3개 모두 사용)

    edges = [["A","B"], ["C","D"]], start = "A"
    → False  (A→B 후 막힘. C-D를 못 씀)
'''
def solution(edges, start):
    graph = {edge[0]: [] for edge in edges}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    path = [start]

    def dfs(vertex):
        if len(edges) + 1 == len(path):
            return True

        for idx in range(len(graph.get(vertex, []))):
            next_vertex = graph[vertex].pop(idx)
            path.append(next_vertex)

            if dfs(next_vertex):
                return True

            path.pop()
            graph[vertex].insert(idx, next_vertex)

        return False