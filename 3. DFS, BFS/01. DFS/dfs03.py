def dfs(i, j, virus):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if i<=0 or i>n or j<0 or j>=n:
        return False
    elif graph[i][j] >= virus:
        graph[i][j] = virus
    dfs(i-1,j, virus)
    dfs(i,j-1, virus)
    dfs(i+1,j, virus)
    dfs(i,j+1, virus)
        
# 3 3
# 1     1(o)  3
# 2     2(o)  3(o)
# 2(o)  0(o)  0(o)

n, k = map(int, input().split())
graph = [[]]
# visited = [[]]
# for i in range(n):
#     visited.append([False]*n)
for i in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
for _ in range(s):
    for i in range(1, n):
        for j in range(n):
            if graph[i][j] > 0:
                dfs(i, j, graph[i][j])
print(graph[x][y-1])
