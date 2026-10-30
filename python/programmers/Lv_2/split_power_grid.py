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
def solution(n, wires):
    graph = {x: [] for x in range(1, n+1)}

    def dfs(parent):
        if parent == []:
            return 1

        return 1 + sum(dfs(graph[i]) for i in parent)

    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    result = 1000

    for i in wires:
        cnt = abs(dfs(graph[1]) - 2*dfs(graph[i[1]]))
        if cnt < result:
            result = cnt

    return result