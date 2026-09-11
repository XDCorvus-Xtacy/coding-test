'''
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 
배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''
def solution(tickets):
    tickets = sorted(tickets, key=lambda x: x[1])
    graph = {ticket[0]: [] for ticket in tickets}
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    visited = 0
    answer = len(tickets) + 1
    path = ["ICN"]
    
    def dfs(airport):
        if len(path) == len(tickets) + 1:
            return True

        for idx in range(len(graph.get(airport, []))):
            next_air = graph[airport].pop(idx)
            path.append(next_air)

            if dfs(next_air):
                return True

            path.pop()
            graph[airport].insert(idx, next_air)

        return False
    
    dfs("ICN")
    return path

# 여행경로 (Programmers Lv.3, DFS/BFS)
# 상태: 코치 유도로 완성 — 백트래킹 핵심부는 자력 도출 못 함. 재현 대상
#
# [스스로 한 것]
# - 그래프 구조 설계 (dict 인접 리스트, 도착지 알파벳 순 정렬)
# - pop으로 항공권을 빼는 발상
# - 막힌 지점 특정: "그 가지가 아니었을 경우 문제가 된다"
#
# [받은 것 — 백트래킹 3요소]
# 1. 되돌리기: 실패하면 graph[a].insert(idx, next) 로 원래 자리에 복구
#              path.pop() 으로 경로도 되돌림
# 2. 성공 신호: dfs가 True/False를 반환해 위로 알림
#              (지금까지 DFS는 반환값이 없었음)
# 3. 성공 판정: len(path) == len(tickets) + 1
#              항공권 n장 = 공항 n+1번 방문
#
# [핵심]
# - 관리 대상이 정점이 아니라 "간선(항공권)"
# - 알파벳 순 정렬 후 탐색하면 처음 완성된 경로가 곧 답
# - 시작점 ICN도 방문한 공항이므로 path = ["ICN"] 으로 시작