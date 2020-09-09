n = int(input("Digite um número para fatoriar: "))
fat=1
while n>=1:
    fat = fat * n
    n-=1

print(f"O resultado do fatorial é: {fat}")