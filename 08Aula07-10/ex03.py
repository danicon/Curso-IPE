Li = []
d=0
while d < 10:
    p = int(input('Digite os números: '))
    if d == 0 or p > Li[-1]:
        Li.append(p)
       
    else:
        for x in range(5):
            if p <= Li[x]:
                Li.insert(x,p)
                break
    d+=1
print(Li[::-1])