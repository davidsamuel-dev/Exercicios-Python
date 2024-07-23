#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0.0

for i in range(0,4):
    notas.append(float(input(f"Insira a {i+1}° nota: ")))

    soma = soma + notas[i]
media = soma / len(notas)

print(f'Suas notas foram: {notas} e a média foi: {media}')

    