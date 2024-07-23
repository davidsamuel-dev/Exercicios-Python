# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numero = []
for x in range(0,5):
    # numero.append(input("Insira o {valor} ° número: ".format(valor = x +1)))
    numero.append(input(f"Insira o {x+1} ° número: "))

print(numero)