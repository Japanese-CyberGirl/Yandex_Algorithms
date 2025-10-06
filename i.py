x, y = map(int, input().split())
f, g = map(int, input().split())

dx = abs(f - x)
dy = abs(g - y)

if dx == 0 and dy == 0:
    print(0)
else:
    if dx == 0 or dy == 0:
        L = 3 * max(dx, dy) - 2
    else:
        L = 3 * (dx + dy) - 4
    print(L - 1)
