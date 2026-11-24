'''
n개의 송전탑이 전선으로 하나의 트리 형태로 연결되어 있습니다.
전선 하나를 끊어 전력망을 2개로 나누려고 하는데, 두 전력망의 송전탑 개수를
최대한 비슷하게 맞추려고 합니다.
두 전력망이 가진 송전탑 개수의 차이(절대값)를 return 하세요.

[제한사항]
- n은 2 이상 100 이하인 자연수
- wires는 길이가 n-1인 2차원 배열
- wires의 각 원소 [v1, v2]는 v1번과 v2번 송전탑이 전선으로 연결되었다는 뜻
- 1 ≤ v1 < v2 ≤ n
- 하나의 트리 형태가 아닌 전력망은 입력으로 주어지지 않음
'''
# solution 1: dfs
def solution_dfs(n, wires):
    graph = {x: [] for x in range(1, n+1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node):
        visited[node] = 1
        cnt = 1

        for nxt in graph[node]:
            if visited[nxt] != 1:
                cnt += dfs(nxt)

        return cnt

    answer = n

    for wire in wires:
        visited = [0]*(n+1)
        visited[wire[0]] = 1
        result = abs(n - 2*dfs(wire[1]))

        if result < answer:
            answer = result

    return answer


print(solution_dfs(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))  # 기대값: 3
print(solution_dfs(4, [[1,2],[2,3],[3,4]]))                                # 기대값: 0
print(solution_dfs(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))              # 기대값: 1
print(solution_dfs(3, [[1,3],[2,3]]))                                      # 기대값: 1
print(solution_dfs(2, [[1,2]]))                                            # 기대값: 0



# solution 2: union-find
def solution_union_find(n, wires):
    def find(a):
        if parent[a] == a:
            return a

        parent[a] = find(parent[a])
        
        return parent[a]

    def combine(a, b):
        parent[find(a)] = find(b)

    result = n

    for i in wires:
        parent = [x for x in range(n+1)]
        for j in wires:
            if i != j:
                combine(j[0], j[1])

        s = 0
        for x in range(1, n+1):
            if find(i[0]) == find(x):
                s += 1
        result = min(result, abs(n - 2*s))

    return result


print(solution_union_find(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution_union_find(4, [[1,2],[2,3],[3,4]]))
print(solution_union_find(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
print(solution_union_find(3, [[1,3],[2,3]]))
print(solution_union_find(2, [[1,2]]))
