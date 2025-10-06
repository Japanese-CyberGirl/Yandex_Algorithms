n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

row_base = [0] * n     
row_q = [0] * n        
col_plus = [0] * m
col_minus = [0] * m
col_q = [0] * m


for i in range(n):
    for j in range(m):
        if matrix[i][j] == '+':
            row_base[i] += 1
            col_plus[j] += 1
        elif matrix[i][j] == '-':
            row_base[i] -= 1
            col_minus[j] += 1
        else:
            row_q[i] += 1
            col_q[j] += 1


col_base_minus_q = [col_plus[j] - col_minus[j] - col_q[j] for j in range(m)]

answer = -10**9


for r in range(n):
    row_sum = row_base[r] + row_q[r] 
    min_col = 10**9


    for j in range(m):

        val = col_base_minus_q[j] + (2 if matrix[r][j] == '?' else 0)
        min_col = min(min_col, val)

    answer = max(answer, row_sum - min_col)

print(answer)
