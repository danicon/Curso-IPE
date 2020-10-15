L = [99,102,89,120,117]
x = 999

for i in range(0,5):
    if L[i] < x:
        x = L[i]
        
print(f"\nO menor número da lista é: {x}")