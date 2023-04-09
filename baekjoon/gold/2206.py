from collections import deque

n, m = map(int, input().split())
graph = []

# 벽을 부순 횟수를 기록하기 위해 3차원 배열 생성
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1  # 시작점 방문 처리

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]  # 상하좌우
dy = [1, -1, 0, 0]  # 상하좌우


def bfs(x, y, z):  # x, y: 현재 위치, z: 벽을 부순 횟수
    queue = deque()  # 큐 생성
    queue.append((x, y, z))  # 큐에 현재 위치와 벽을 부순 횟수를 넣음

    while queue:
        a, b, c = queue.popleft()  # 큐에서 하나씩 빼냄
        if a == n - 1 and b == m - 1:  # 도착지점에 도착한 경우
            return visited[a][b][c]
        for i in range(4):  # 상하좌우 이동
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위를 벗어나는 경우
                continue
            if graph[nx][ny] == 1 and c == 0:  # 벽을 만난 경우
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:  # 벽이 아닌 경우
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))  # 시작점에서 벽을 부수지 않은 상태로 시작
