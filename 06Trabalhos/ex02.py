# Faça uma solução lógica em Python que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.
# Código
# Cargo
# Percentual
# 1
# Operador
# 28%
# 2
# Secretário
# 17%
# 3
# Caixa
# 10%
# 4
# Gerente
# 25%
# 5
# Supervisor
# 36%
# 6
# Diretor
# 18%
# 7
# CEO
# 76%

sal_atual = float(input('Digite o seu salário atual: '))
codigo = int(input('Digite o seu código de 1 ao 7: '))
if codigo == 1:
    cal = sal_atual * 1.28
    car = 'Operador'
    print(f'{car} - Receberá um aumento de 28%, totalizando em R${cal}')
elif codigo == 2:
    cal = sal_atual * 1.17
    car = 'Secretário'
    print(f'{car} - Receberá um aumento de 17%, totalizando em R${cal}')
elif codigo == 3:
    cal = sal_atual * 1.10
    car = 'Caixa'
    print(f'{car} - Receberá um aumento de 10%, totalizando em R${cal}')
elif codigo == 4:
    cal = sal_atual * 1.25
    car = 'Gerente'
    print(f'{car} - Receberá um aumento de 25%, totalizando em R${cal}')
elif codigo == 5:
    cal = sal_atual * 1.36
    car = 'Supervisor'
    print(f'{car} - Receberá um aumento de 36%, totalizando em R${cal}')
elif codigo == 6:
    cal = sal_atual * 1.18
    car = 'Diretor'
    print(f'{car} - Receberá um aumento de 18%, totalizando em R${cal}')
elif codigo == 7:
    cal = sal_atual * 1.76
    car = 'CEO'
    print(f'{car} - Receberá um aumento de 76%, totalizando em R${cal}')
else:
    print('\n [ERRO] - Código invalido, tente novamente... \n')