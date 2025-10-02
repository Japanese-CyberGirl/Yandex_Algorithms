def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n , k):
    return factorial(n) // (factorial(k) * factorial(n - k))

s = str(input())

counts = {}

for i in s:
    counts[i] = counts.get(i, 0) + 1

n = len(s)

answer = combinations(n , 2)

for count in counts.values():
    answer -= combinations(count, 2)

print(answer + 1)