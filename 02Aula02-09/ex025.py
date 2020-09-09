fumante = int(input('\n Quantos cigarros por dia você fuma? \n'))
anos = float(input('\n Quantos anos de fumante? \n'))
vida = (fumante * anos)-10

print('\n Você fuma {0} cigarros por dia e já é fumante a {1} anos. Você perdeu {2} dias de vida \n'.format(fumante, anos, vida)
)