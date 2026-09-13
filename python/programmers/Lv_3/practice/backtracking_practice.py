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