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

tot = T[0] + T[1] + T[2] + T[3] + T[4] + T[5] + T[6] + T[7] 

media = tot / 8

print(f'A média da temperatura é: {media}')

