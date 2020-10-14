v = [9, 8, 7, 11, 12, 23, 21, 22]
p = []
i = []

for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)
print(v)
print(p)
print(i)