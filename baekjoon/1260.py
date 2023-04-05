import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]  # 인접 리스트
visited = [False] * (n+1)  # 방문 여부

for _ in range(m):  # 간선 정보 입력
    a, b = map(int, input().split())  # a와 b가 연결되어 있음
    graph[a].append(b)  # 양방향 그래프
    graph[b].append(a)  # 양방향 그래프

for i in range(n+1):  # 정점 번호가 작은 것을 먼저 방문
    graph[i].sort()  # 오름차순 정렬


def dfs(v):  # 깊이 우선 탐색
    visited[v] = True  # 방문 처리
    print(v, end=' ')  # 방문한 정점 출력
    for i in graph[v]:  # 인접한 정점들을 순회
        if not visited[i]:  # 방문하지 않은 정점이라면
            dfs(i)  # 재귀적으로 방문


def bfs(v):  # 너비 우선 탐색
    queue = [v]  # 큐 생성
    visited[v] = False  # 방문 처리
    while queue:  # 큐가 비어있지 않다면
        v = queue.pop(0)  # 큐에서 하나를 꺼냄
        print(v, end=' ')  # 방문한 정점 출력
        for i in graph[v]:  # 인접한 정점들을 순회
            if visited[i]:  # 방문하지 않은 정점이라면
                queue.append(i)  # 큐에 삽입
                visited[i] = False  # 방문 처리


dfs(v)  # 깊이 우선 탐색
print()  # 줄바꿈
bfs(v)  # 너비 우선 탐색
