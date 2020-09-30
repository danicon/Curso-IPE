import os
os.system('cls')

saida = 0
while saida <= 204:

    print('\n ----------------Menu--------------- \n' )
    print(' Multiplicação = "*" \n Subtração = "-" \n Divisão = "/" \n Adição = "+" \n Sair = "S" \n' )
    oper = input('Digite a operação: ')

    if oper == '+':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1 + n2
        print(f'\n O resultado da soma de {n1} + {n2} é: {res}! \n')
    elif oper == '-':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1 - n2
        print(f'\n O resultado da subtração de {n1} - {n2} é: {res}! \n')
    elif oper == '/':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1 / n2
        print(f'\n O resultado da divisão de {n1} / {n2} é: {res}! \n')
    elif oper == '*':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1 * n2
        print(f'\n O resultado da multiplicação de {n1} x {n2} é: {res}! \n')
    elif oper == 's' or oper == 'S':
        saida = 205
        print('\n -------------Até a próxima!!!-------------- \n')
    else:
        print('\n [ERRO] - O valor digitado é invalido, tente novamento... \n')

saida += 1