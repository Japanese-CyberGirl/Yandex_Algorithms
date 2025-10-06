n , k = map(int, input().split())

n1 = n
for i in range(k):
    n += n%10
print(n)

