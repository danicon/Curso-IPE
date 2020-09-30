# Faça uma solução lógica em Python que leia um valor N inteiro e positivo. Calcule e mostre o valor de E, conforme a fórmula a seguir:
# E = 1 + 1/N! ... + 1/3! + 1/2! + 1/1!

n = int(input('Digite um valor inteiro e positivo: '))

if n > 0:  
    fat = 1
    fat2 = 1
    fat3 = 1
    fat4 = 1
    p = 3
    q = 2
    u = 1 
    while n >=1:
        fat = fat * n
        n-=1
    while p >=1:
        fat2 = fat2 * p
        p-=1
    while q >=1:
        fat3 = fat3 * q
        q-=1
    while u >=1:
        fat4 = fat4 * u
        u-=1

    e = 1 + 1 / fat + 1 / fat2 + 1 / fat3 + 1 / fat4 
    print(f'\nO calculo da equação: E = 1 + 1/{fat}! + 1/{fat2}! + 1/{fat3}! + 1/{fat4}! = {e:.3f}\n')
else: 
    print('\n [ERRO] - O número digitado não um valor inteiro e positivo!! \n')    
