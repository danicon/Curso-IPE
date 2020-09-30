# Faça um a solução lógica em Python para um funcionário de uma empresa que recebe, anualmente, aumento salarial.
# Sabe-se que:
# a) Esse funcionário foi contratado em 2015, com salário inicial de R$ 2.000,00.
# b) Em 2016, ele recebeu aumento de 0,5% sobre seu salário inicial.
# c) A partir de 2017 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.

print('\nEsse funcionário foi contratado em 2015, com salário inicial de R$2.000 \n')
sal = 2010
ano = 2016
porcent = 0.5
while ano <= 2020:
    print(f'O salário em {ano} passou a valer R${sal:.2f}\n')
    porcent = porcent * 2
    sal = sal + (sal * porcent / 100)
    ano += 1
    
