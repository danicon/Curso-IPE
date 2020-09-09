altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
if altura < 1.20:
    if peso <= 60:
        print('CLASSIFICAÇÃO "A"')
    elif 60 < peso <= 90:
        print('CLASSIFICAÇÃO "D"')
    elif peso > 90:
        print('CLASSIFICAÇÃO "G"')
elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        print('CLASSIFICAÇÃO "B"')
    elif 60 < peso <= 90:
        print('CLASSIFICAÇÃO "E"')
    elif peso > 90:
        print('CLASSIFICAÇÃO "H"')
elif altura > 1.70:
    if peso <= 60:
        print('CLASSIFICAÇÃO "C"')
    elif 60 < peso <= 90:
        print('CLASSIFICAÇÃO "F"')
    elif peso > 90:
        print('CLASSIFICAÇÃO "I"')