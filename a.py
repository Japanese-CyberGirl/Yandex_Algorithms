n = int(input())

lst = list(map(int, input().split()))

even_sub = sorted([lst[i] for i in range(len(lst)) if i % 2 == 0])
odd_sub = sorted([lst[i] for i in range(len(lst)) if i % 2 != 0])

print(max(sum(even_sub) - sum(odd_sub), sum(even_sub) - sum(odd_sub) + 2 * max(odd_sub) - 2 * min(even_sub)))