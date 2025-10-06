n , k = map(int, input().split())

vector = list(map(int, input().split()))

themes = {}

for i in vector:
    themes[i] = themes.get(i, 0) + 1

#print(themes)

if (k <= len(themes)):
    counter = 0
    for i in themes.keys():
        if counter >= k:
            break
        print(i, end = ' ') 
        counter += 1 

if (k > len(themes)):
    for i in themes.keys():
        print(i, end = ' ')
    counter = k - len(themes)
    for i in themes.keys():
        themes[i] -= 1
    for i in vector:
        if themes[i] > 0:
            while (themes[i] > 0) :
                if counter == 0:
                    break
                print(i, end = ' ')
                themes[i] -= 1
                counter -= 1
