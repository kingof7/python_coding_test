1. 스택 자료구조 > 파이썬에서 리스트
입구와 출구가 동일한 형태로 스택을 시각화할 수 있음.

LIFO
c    c
▽   △
b    b
a    a

ex:)

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack[::-1]) # 최상단 원소(맨 마지막)부터 출력
print(stack)       # 최하단(가장 먼저 삽입된) 원소부 출력

2. 큐 자료구조
FIFO 

popleft()             append(<?>) 
      ---------------
1 <== | (1) 2 3 (4) | <== 4
      ---------------
from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

3. 재귀 함수 (자기 자신을 다시 호출)
# 재귀 종료 조건이 없는 경우
# ex
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()
recursive_function()

# 재귀함수의 종료 조건을 반드시 명시해야함
# ex
def recursive_function(i):
    if i == 100:
        print(i, '번째 재귀함수를 호출하지 않고 종료합니다.')
        return
    print('재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째부터 재귀함수 종료 시작 - stack')
    print(i, '번째 재귀함수를 종료합니다.')
recursive_function(1)

