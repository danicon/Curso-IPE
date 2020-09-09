km = float(input('\n Quantos Km o carro percorreu? \n'))
dias = int(input('\n Quantos dias de uso do carro alugado? \n'))
alugado = (0.15 * km) + (60 * dias)

res = '\n O carro alugado por {0} dias, percorridos por {1} km/h. Totalizou em R${2} \n'.format(dias, km, alugado)

print(res)