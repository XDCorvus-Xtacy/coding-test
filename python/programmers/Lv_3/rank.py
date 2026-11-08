'''
n명의 권투선수가 1:1 경기를 했습니다. 실력이 더 좋은 선수는 항상 이깁니다.
몇몇 경기 결과를 분실해서 정확한 순위를 매길 수 없는 선수도 있습니다.
선수의 수 n, 경기 결과 results가 주어질 때, 정확하게 순위를 매길 수 있는 선수의 수를
return 하세요.

[제한사항]
- 선수의 수는 1명 이상 100명 이하
- 경기 결과는 1개 이상 4,500개 이하
- results의 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 뜻
- 모든 경기 결과에는 모순이 없음

[입출력 예]
n    results                                   return
5    [[4,3],[4,2],[3,2],[1,2],[2,5]]           2
'''
def solution(n, results):
    winner_graph = {x: [] for x in range(1, n+1)}
    loser_graph = {x: [] for x in range(1, n+1)}

    for a, b in results:
        winner_graph[a].append(b)
        loser_graph[b].append(a)

    def dfs(number, graph):
        visited[number] = 1
        cnt = 1

        for nxt in graph[number]:
            if visited[nxt] != 1:
                cnt += dfs(nxt, graph)

        return cnt

    answer = 0

    for i in range(1, n+1):
        visited = [0]*(n+1)
        win = dfs(i, winner_graph)
        visited = [0]*(n+1)
        lose = dfs(i, loser_graph)

        if win+lose-1 == n:
            answer += 1

    return answer

print(solution(5, [[4,3],[4,2],[3,2],[1,2],[2,5]]))   # 기대값: 2 (공식 예시)
print(solution(3, [[1,2],[2,3]]))                     # 기대값: 3 (일렬: 모두 확정)
print(solution(4, [[1,2],[3,4]]))                     # 기대값: 0 (두 무리로 나뉨)
print(solution(2, [[2,1]]))                           # 기대값: 2 (가장 작은 입력)
print(solution(4, [[1,2],[1,3],[2,4],[3,4]]))         # 기대값: 2 (1, 4번만 확정)