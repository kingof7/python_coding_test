# 유클리드 호제법
# A > B 인 경우, A와 B의 최대공약수는
# B와 A를 B로나눈 나머지 R의 최대공약수와 같다.
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
print(gcd(192, 162))

