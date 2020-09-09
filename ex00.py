altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
if altura < 1.20:
    if peso <= 60:
        print('CLASSIFICAÇÃO: A')
    elif peso <= 90:
        print('CLASSIFICAÇÃO: D')
    elif peso > 90:
        print('CLASSIFICAÇÃO: G')
elif altura <= 1.70:
    if peso <= 60:
        print('CLASSIFICAÇÃO: B')
    elif peso <= 90:
        print('CLASSIFICAÇÃO: E')
    elif peso > 90:
        print('CLASSIFICAÇÃO: H')
else:
    if peso <= 60:
        print('CLASSIFICAÇÃO: C')
    elif peso <= 90:
        print('CLASSIFICAÇÃO: F')
    else:
        print('CLASSIFICAÇÃO: I')