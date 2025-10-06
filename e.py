n , k = map(int, input().split())

lst = []
counter = 0
flag = False

for i in range(k):
    x = n % 10

    if (x in lst):
        start = lst.index(x)
        cycle = lst[start:]
        counter = i
        flag = True
        break
    lst.append(x)
    n += x

if (flag):

    dlina = len(lst[start:])
    amount = sum(lst[start:])

    middle_iterations = (k - counter)//dlina
    last_iterations = k - counter - middle_iterations * dlina

    n += amount * middle_iterations

    for i in range(last_iterations):
        n += n % 10


print(n)
