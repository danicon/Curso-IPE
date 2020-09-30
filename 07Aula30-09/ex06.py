altura = []
x=0
while x < 8:
    altura.insert(x, float(input('Digite a sua altura: ')))
    x+=1

res = (altura[0] + altura[1] + altura[2] + altura[3] + altura[4] + altura[5] + altura[6] + altura[7]) / len(altura)

print(f'A média das alturas apresentadas é: {res}')

