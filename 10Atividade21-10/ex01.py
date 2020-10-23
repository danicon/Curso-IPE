par = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
imp = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
tot = []

tot = par + imp

for e in tot:
    print(e)

print('\n\n')

fim = len(tot)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if tot[x] > tot[x + 1]:
            trocou = True
            temp = tot[x]
            tot[x] = tot[x + 1]
            tot[x + 1] = temp
        x+=1
    if not trocou:
        break
    fim -= 1

for e in tot:
    print(e)