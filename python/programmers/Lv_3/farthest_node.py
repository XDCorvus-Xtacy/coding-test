'''
n개의 노드가 있는 그래프에서 1번 노드로부터 가장 멀리 떨어진 노드의 개수를 구하려 합니다.
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
노드의 개수 n, 간선 정보 vertex가 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가
몇 개인지 return 하세요.

[제한사항]
- 노드의 개수 n은 2 이상 20,000 이하
- 간선은 양방향이며 총 1개 이상 50,000개 이하
- vertex의 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 뜻

[입출력 예]
n    vertex                                                 return
6    [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]            3
'''
from collections import deque
def solution(n, edge):
    graph = {x: [] for x in range(1, n+1)}
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(q):
        while q:
            cur = q.popleft()
            if visited[cur[1]] == 0:
                visited[cur[1]] = cur[0]
                for i in graph[cur[1]]:
                        q.append((cur[0]+1, i))
        return visited.count(cur[0]-1)

    q = deque()
    for i in graph[1]:
        q.append((1, i))
    visited = [-1,-1] + [0]*(n-1)

    return bfs(q)
