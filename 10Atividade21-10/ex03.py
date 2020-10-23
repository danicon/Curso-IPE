L1 = [7, 4, 3, 12, 8]
L2 = [6, 2, 0, 14, 10]
L3 = []

for e in L1:
    print(e)

print('\n\n')

fim = len(L1)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L1[x] > L1[x + 1]:
            trocou = True
            temp = L1[x]
            L1[x] = L1[x + 1]
            L1[x + 1] = temp
        x+=1
    if not trocou:
        break
    fim -= 1

for e in L1:
    print(e)

print('\n==============\n')   

for e in L2:
    print(e)

print('\n\n')

fim = len(L2)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L2[x] > L2[x + 1]:
            trocou = True
            temp = L2[x]
            L2[x] = L2[x + 1]
            L2[x + 1] = temp
        x+=1
    if not trocou:
        break
    fim -= 1

for e in L2:
    print(e)

print('\n==============\n')

L3 = L1 + L2 

for e in L3:
    print(e)

print('\n\n')

fim = len(L3)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L3[x] > L3[x + 1]:
            trocou = True
            temp = L3[x]
            L3[x] = L3[x + 1]
            L3[x + 1] = temp
        x+=1
    if not trocou:
        break
    fim -= 1

for e in L3:
    print(e)