# 최단 거리 문제는 BFS로 푼다
# 가장 가까운 노드부터 차례대로 방문
# 이전 거리에 +1하면서 최단거리 구함

# 1)
# 1 1 0
# 0 1 0
# 0 1 1

# 2)
# 1 (2) 0 +1
# 0  1  0
# 0  1  1

# 3)
# 1  2  0
# 0 (3) 0 +1
# 0  1  1

# 4)
# 1  2  0
# 0  3  0
# 0 (4) 1 +1

# 3)
# 1 2  0
# 0 3  0
# 0 4 (5) +1 ==> 최단거리는 5
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if queue[nx][ny] == 0:
                continue
            if queue[nx][ny] == 1:
                queue[nx][ny] = queue[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1] # 우측 맨 하단, 마지막 값

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

print(bfs(0,0))

