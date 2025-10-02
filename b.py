a , b , c , v0 , v1 , v2 = map(int, input().split())

answer = 0

roads = [a , b , c]

dDS = min(a, b + c)
dDP = min(b, a + c)
dSP = min(c, a + b)

t1 = dDS / v0 + dSP / v1 + dDP / v2
t2 = dDP / v0 + dSP / v1 + dDS / v2
t3 = dDS / v0 + dDS / v1 + dDP / v0 + dDP / v1
t4 = dDP / v0 + dDP / v1 + dDS / v0 + dDS / v1

print(min(t1, t2, t3, t4))