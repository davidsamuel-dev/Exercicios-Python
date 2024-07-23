# Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.
nome = input("Insira um nome: ")
qtd_c = 0
qtd_v = 0


for i in range(0, len(nome)):
    
    l = nome[i].upper()
    print(l)
    if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
        qtd_v = qtd_v + 1
    else:
        qtd_c = qtd_c + 1
        
print(f"esse texto possui: \n{qtd_c} consooantes\n{qtd_v} vogais" )