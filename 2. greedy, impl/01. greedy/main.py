# 그리디 문제

# 온라인 코테 library 사용 방법 검색 가능
# 오프라인 코테 설치된 환경을 이용
# 온라인 저지
# 해외 : 코드포스, 탑코더, 릿코드, 코드셰프
# 국내 : 백준(대기업 기출이 가장 많음)
# , 코드업(초보자)
# , 프로그래머스(대기업 + 다양함), SWEA(삼성 코테 준비)
# 파이썬 튜터 : 비쥬얼라이져

# 그리디알고리즘(탐욕)
# 1. 가장 좋은거(큰거)를 먼저 고르는 것
# 2. 큰 단위가 작은 단위의 배수일 경우에만 적용 가능
# ex:) 500원 100원 50원 10원 > 100*5 = 500 / 50*10 = 500 / 10*50 = 500

# Q1.
# n = 1260
# count = 0
# arr = [500, 100, 50, 10]
# for coin in arr:
#    count += n // coin
#    n %= coin
# print("총 코인의 수는 " + str(count) +"개")

# Q2.
# n, k = map(int, input().split())
# result = 0
# while True:
#     #19 , 3
#     target = (n // k) * k
#     result += n - target
#     if n < k: break
#     result = result + 1
#     n //= k
# result += (n - 1)
# print(result)

# Q3.
# 두 수에 대해 연산을 수행할 때, 두 수 중 하나라도 1이하인 경우는 더하고, 두수가 모두 2이상이면 곱한다
# data = input()
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <=1 or result <=1:
#         result += num
#     else:
#         result *= num
# print(result)

# n = input()
# length = len(str(n)) - 1
# sum = int(n[0])
# for i in range(length):
#     if int(n[i])<=1 or int(n[i+1])<=1:
#         sum += int(n[i+1])
#     elif int(n[i])>=1 and int(n[i+1])>=1:
#         sum *= int(n[i+1])
# print(sum)


# n = input()
# length = len(str(n)) - 1

# # 02984
# sum = int(n[0])

# for i in range(length):
#     tmp = sum + int(n[i+1])
#     tmpCross = sum * int(n[i+1])
#     if(tmp > tmpCross):
#        sum = tmp
#     else:
#        sum = tmpCross

# print(sum)

# Q4
# 모험가의 수 n
# 모험가의 공포도가 a라면 각 그룹에는 최소 a명이 있어야함
# 각 그룹에는 최소의 모험가만 있어야함 ( 같은 공포도를 가진 모험가 들 )
# 그룹 수의 최대값 구하기
n = int(input())
data = list(map(int, input().split())) # 모험가의 공포도
data.sort() # 오름차순 정렬

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

# 2 3 1 2 4
# 1 2 2 3 4
# (1) (2 2) 3 4
# 2 그룹


