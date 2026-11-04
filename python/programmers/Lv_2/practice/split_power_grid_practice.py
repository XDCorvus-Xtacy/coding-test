# 전력망을 둘로 나누기 — 계단 학습
# 계단 1: 끊기 없이, 출발점에서 갈 수 있는 송전탑 개수 세기 (예시 2 그래프)

graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
visited = [0] * 5

def dfs(number):
    visited[number] = 1
    cnt = 1

    for nxt in graph[number]:
        if visited[nxt] != 1:
            cnt += dfs(nxt)

    return cnt

print(dfs(1))   # 기대값: 4     실행값: 4
visited = [0] * 5
print(dfs(4))   # 기대값: 4     실행값: 4



# 계단 2: 전선 [2, 3]을 끊었을 때 3번 쪽 송전탑 수 (graph·dfs는 그대로)
# 트리이므로 3번 쪽에서 2번으로 가는 길은 끊은 전선 하나뿐
visited = [0] * 5
visited[2] = 1

print(dfs(3))   # 기대값: 2     실행값: 2
visited = [0] * 5


# 계단 3: 전선을 하나씩 끊으며 b 쪽 개수와 차이 출력 (예시 2)
'''
s     전선 [a, b]를 끊었을 때 b번 쪽에 있는 송전탑 수
      (계단 2의 dfs(3)과 같은 값 → 그때는 a = 2, b = 3)

diff  그때 두 전력망의 송전탑 수 차이 (절댓값)
      b 쪽이 s개면 a 쪽은 몇 개일지 생각해서 구하면 됩니다
'''
n = 4
wires = [[1, 2], [2, 3], [3, 4]]

for a, b in wires:
    visited = [0] * 5
    visited[a] = 1
    s = dfs(b)
    diff = abs(n - 2*s)

    print(a, b, s, diff)



# 계단 4: 계단 1~3을 함수로 (graph는 wires로 직접 만들기)
def solution(n, wires):
    pass


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))   # 기대값: 3
print(solution(4, [[1,2],[2,3],[3,4]]))                                 # 기대값: 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))               # 기대값: 1