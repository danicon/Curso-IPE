L = [8, 6, 16, 1, 5, 11, 0, 2, 14, 7]

for e in L:
    print(e)

print('\n\n')

fim = len(L)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x+=1
    if not trocou:
        break
    fim -= 1

L = L[::-1]
for e in L:
    print(e)