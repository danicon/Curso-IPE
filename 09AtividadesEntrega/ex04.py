L = [99,102,89,120,117]
x = 0

for i in range(0,5):
    if L[i] > x:
        x = L[i]
        
print(f"\nO maior número da lista é: {x}")