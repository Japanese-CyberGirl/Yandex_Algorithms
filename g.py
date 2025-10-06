n, m = map(int, input().split())

matrix = [input().strip() for _ in range(n)]

found = False


for i in range(n):
    row = matrix[i]
    
    for j in range(m - 4):
        if row[j] != '.' and row[j:j+5] == row[j] * 5:
            found = True
            break
    if found:
        break


if not found:
    for j in range(m):
        col = ''.join(matrix[i][j] for i in range(n))
        for i in range(n - 4):
            if col[i] != '.' and col[i:i+5] == col[i] * 5:
                found = True
                break
        if found:
            break


if not found:
    for i in range(n - 4):
        for j in range(m - 4):
            s = matrix[i][j]
            if s != '.' and all(matrix[i+k][j+k] == s for k in range(5)):
                found = True
                break
        if found:
            break


if not found:
    for i in range(4, n):
        for j in range(m - 4):
            s = matrix[i][j]
            if s != '.' and all(matrix[i-k][j+k] == s for k in range(5)):
                found = True
                break
        if found:
            break

print('Yes' if found else 'No')
