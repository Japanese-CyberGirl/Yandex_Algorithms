n, m = map(int, input().split())

s = input().strip()

parts = []
for i in range(m):
    parts.append(input().strip())

k = n // m  

result = []

used = [False] * m  

for i in range(0, n, k):
    sub = s[i:i+k]
    for j in range(m):
        if not used[j] and parts[j] == sub:
            result.append(j + 1)
            used[j] = True
            break

print(*result)
