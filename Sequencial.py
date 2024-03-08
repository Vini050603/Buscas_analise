# TRABALHO BUSCA SEQUENCIAIS

import random
# Variaveis globais
lista = []
chaves = []
n = 10  # quantidade de números na sequencia

# busca sequencial
def busca_sequencial(sequencia, chave):
    for v in range(len(sequencia)):
        if sequencia[v] == chave:
            return chave
    return -1

# Quantidade de chaves a serem encontradas
q = int(input("Número de chaves a serem encontradas:"))

# Criando lista com valores aleatórios
for w in range(n):
    lista.append(random.randint(0, 100))

# Criando chaves com valores aleatórios
for w in range(q):
    chaves.append(random.randint(0, 100))

for w in range(q):

    #Chama busca sequencial
    resultado = busca_sequencial(lista, chaves[w])

    #Verificação do elemento
    if resultado != -1:
        print(f'O elemento {chaves[w]} foi encontrado no índice {w}.')
    else:
        print(f'O elemento {chaves[w]} não está na lista.')