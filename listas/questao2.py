# Faça um Programa que leia um vetor de 10 números reais 
# e mostre-os na ordem inversa.

numeros = []

for x in range(0,10):
    numeros.append(input(f'Insira o {x+1}° número: '))

numeros.reverse()
print(numeros)