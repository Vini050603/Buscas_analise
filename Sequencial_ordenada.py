#BUSCA SEQUENCIAL ORDENADA

import random

# Variaveis globais
lista = []
chaves = []
n = 10  # quantidade de números na sequencia


# busca sequencial
def busca_sequencial(sequencia, chave):
    for indice, valor in enumerate(sequencia):
        if valor == chave:
            return indice
    return -1


# Quantidade de chaves a serem encontradas
q = int(input("Número de chaves a serem encontradas:"))

# Criando lista com valores aleatórios
for _ in range(n):
    lista.append(random.randint(0, 20))

# Criando chaves com valores aleatórios
for _ in range(q):
    chaves.append(random.randint(0, 20))

#Ordenando lista
lista = sorted(lista)

for w in range(q):

    # Chama busca sequencial
    resultado = busca_sequencial(lista, chaves[w])

    # Verificação do elemento
    if resultado != -1:
        print(f'O elemento {chaves[w]} foi encontrado no índice {resultado}.')
    else:
        print(f'O elemento {chaves[w]} não está na lista.')

