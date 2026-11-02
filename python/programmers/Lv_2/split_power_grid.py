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

[입출력 예]
n    wires                                              result
9    [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]  3
4    [[1,2],[2,3],[3,4]]                                0
7    [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]              1
'''
# 버린 설계 1: 유니온-파인드로 합친 뒤 이정표를 바꿔 끊기 → 굳이 반복하지 않고 한번에 하는 길이 보여서
# 버린 설계 2: 대표 대신 "다음 정점"을 기록 → 유니온-파인드를 버리면서 버림
# 버린 설계 3: 그래프를 한 방향(v1 → v2)으로만 기록 → 한 방향으로만 기록하면 root를 못 찾음

def solution_dfs(n, wires):
    graph = {x: [] for x in range(1, n+1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(number):
        visited[number] = 1
        cnt = 1
        for nxt in graph[number]:
            if visited[nxt] == 0:
                cnt += dfs(nxt)
        return cnt

    result = n
    for a, b in wires:
        visited = [0] * (n+1)   # ① 전선마다 새로
        visited[a] = 1          # ② 끊은 전선의 반대쪽 끝을 막음
        s = dfs(b)              # b 쪽 송전탑 수
        result = min(result, abs(n - 2*s))   # ③ 반대쪽 = n - s
    return result