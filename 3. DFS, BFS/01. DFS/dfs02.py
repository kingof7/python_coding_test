# dfs는 재귀적으로 상하좌우 계속 방문한다 모두 방문 하면 +1

# 00110
# 00011
# 11111
# 00000

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 현재 위치로부터 좌상우하 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # 모두 방문했으면 True (아이스크림이 1 덩이 만들어 졌을시점)
    return False


n, m = map(int, input().split()) # 행, 열 받고
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 행 만큼 리스트 넣음
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(i, j)
            cnt += 1 # 아이스크림 1덩이 만들어질 때마다 ++1
print(cnt) # 결과


