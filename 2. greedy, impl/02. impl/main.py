# 구현(implementation)
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# dx = [0,0,-1,1]
# dy = [-1, 1, 0, 0]
# move_types = ['L','R','U','D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#         if nx < 1 or ny < 1 or nx > n or ny > n:
#             continue
#         x, y = nx, ny
# print(x, y)

# Q2
# 모든 시각 중 3이 하나라도 포함되는 모든 경우 수
# 00시 00분 00초 ~ N시 59분 59초
# h = int(input())
# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count += 1
# print(count)

# Q3.
# print(ord("a"))
# a는 97
# 1. L L U / L L D
# 2. R R U / R R D
# 3. U U L / U U R
# 4. D D L / D D R
# a1 
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
# steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
#         result += 1
# print(result)

# x = input()
# count = 0
# move = [-1, 1]
# for i in range(4):
#     for j in range(2):
#         dx = int(x[1])
#         dy = ord(x[0]) - 95
#         if i < 2:
#             dx += 2*move[i]
#             if j == 0:
#                 dy -= 1
#             else:
#                 dy += 1
#         else:
#             if i == 2:
#                 dy -= 2
#             else:
#                 dy += 2
#             if j == 0:
#                 dx -= 1
#             else:
#                 dx += 1               
#         if dx >=1 and dx <= 8 and dy >=1 and dy <= 8:
#             count += 1
# print(count)

# Q4.
data = input()
result = []
value = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0: # 0이아닌경우 체크필요
    result.append(str(value))
print(''.join(result))

# string = input()
# alpha = ''
# result = ''
# sum = 0
# for char in string:
#     if ord(char) < 65:
#        sum += int(char)
#     else:
#         alpha += char
# result = ''.join(sorted(alpha))
# if sum != 0:
#     result += str(sum)
# print(result)
