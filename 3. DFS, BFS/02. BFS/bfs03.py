# 백준 18352
# https://www.acmicpc.net/problem/18352
from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]   # 인접 노드 표현 2차원 그래프
distance = [0] * (n+1)             # 노드 까지의 누적거리
visited = [False] * (n+1)          # 노드 방문여부

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)             # a에 인접한 노드 설정(=b)
print(distance)
print(visited)
print(graph)

def bfs(start):
    answer = []
    q = deque([start])             # 시작할 노드를 큐에 넣고
    visited[start] = True          # 시작노드 방문 처리
    distance[start] = 0            # 시작할 노드는 자기 자신이므로 0으로 거리 초기화
    while q:
        now = q.popleft()          # now번째부터 인접 노드 모두 확인
        for i in graph[now]:       # now번째 간선과 인접한 모든 노드 확인
            if not visited[i]:                    # 인접한 노드 중 방문하지 않은 노드일 경우
                visited[i] = True                 # 방문처리
                q.append(i)                       # q에 인접노드 넣기 > 다시 재시작하기위해
                distance[i] = distance[now] + 1   # 인접노드까지 누적된 거리
                if distance[i] == k:              # 누적거리가 k일 경우
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()              # 오름차순 정렬
        for i in answer:
            print(i, end='\n')     # 개행하지 않고 print

bfs(x)