# dfs는 stack 구현과 같다. (재귀)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],      # 0번은 비워두자 // 인덱스랑 노드를 매핑하기 위함
    [2,3,8], # 1번노드와 연결되어있는 노드
    [1,7],   # 2번노드와 연결되어있는
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False] * 9 # 0 인덱스를 사용하지 않기 위해 최대 노드보다 1 더 크게 만들어 줌

dfs(graph, 1, visited) # 첫번째 노드부터 시작

    