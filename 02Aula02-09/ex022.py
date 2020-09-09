n1 = float(input("\n Digite a sua primeira nota: \n"))
n2 = float(input("\n Digite a sua segunda nota: \n"))
media = (n1+n2)/2


if media >= 7:
    print('\n Você está Aprovado com a média de {0} \n'.format(media))
else:
    print('\n Você está Reprovado com a média de {0} \n'.format(media))