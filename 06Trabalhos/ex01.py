# Faça uma solução lógica em Python para resolver a o problema do Pedro, que comprou um saco de ração com peso em quilos. Ele possui três gatos, para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. Faça uma lógica que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após sete dias.

kilo = float(input('Digite os quilos de ração: '))
gato1 = float(input('Digite o consumo diário de ração para o primeiro em gramas: '))
gato2 = float(input('Digite o consumo diário de ração para o segundo em gramas: '))
gato3 = float(input('Digite o consumo diário de ração para o terceiro em gramas: '))
quant1 = gato1 / 1000 * 7
quant2 = gato2 / 1000 * 7
quant3 = gato3 / 1000 * 7
res = kilo - quant1 - quant2 - quant3
print(f'\nRestaram {res:.1f} Kg de ração após 7 dias de consumo por três gatos')