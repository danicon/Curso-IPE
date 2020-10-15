print('\n')
T = [-10, -8, 0, 1, 2, 5, -2, -4]

x = 0

for i in range(0,8):
    if T[i] > x:
        x = T[i]
print(f'{T}\n')        
print(f"A maior temperatura é: {x}\n")

x = 999

for i in range(0,8):
    if T[i] < x:
        x = T[i]
        
print(f"A menor temperatura é: {x}\n")

soma = 0

for i in T:
    soma = soma + i
media = soma / len(T)

print(f'A média da temperatura é: {media}')