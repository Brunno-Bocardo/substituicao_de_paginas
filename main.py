#####################################
#        LEITURA DO ARQUIVO         #
#####################################

def ler_arquivo(arquivo):                                         # Recebe o arquivo
    try:                                                          # Tenta abrir o arquivo
        with open(arquivo, 'r') as file:                          # Abre o arquivo e executa a leitura ('r' -> read)
            linhas = file.read().splitlines()                     # Lê o arquivo e divide em linhas
        return linhas
    except FileNotFoundError:                                     # Se não encontrar o arquivo
        print(f"O arquivo '{arquivo}' não foi encontrado.")
        return None

arquivo = 'arquivo.txt'                                           # Diz qual o arquivo
linhas = ler_arquivo(arquivo)                                     # Chama a função pra ler o arquivo

if linhas is not None:                                            # Se o arquivo tiver sido encontrado
    capacidade = int(linhas[0])                                   # Pega a primeira linha
    paginas = [int(pagina) for pagina in linhas[1:]]              # Cria um vetor com as outras linhas ([1:] = índice 1 pra frente)


#####################################
#       IMPLEMENTAÇÃO DO FIFO       #
#####################################

def fifo():
    espaco_de_memoria = []                                        # Vetor que representa o espaço disponível na memória
    fifo_falta_de_pagina = 0                                      # Contador das faltas de página

    for pagina in paginas:                                        # Passa pelo vetor das páginas
        if pagina not in espaco_de_memoria:                       # Se uma página não está na memória
            if len(espaco_de_memoria) == capacidade:              # Se a memória já está cheia
                espaco_de_memoria.pop(0)                          # Elimina o primeiro elemento do vetor (pop)
            espaco_de_memoria.append(pagina)                      # Adiciona a página atual no (final) espaço disponível na memória 
            fifo_falta_de_pagina += 1                             # Incrementa a falta de página

    return fifo_falta_de_pagina                                   # Retorna o número de falta de páginas


#####################################
#       IMPLEMENTAÇÃO DO LRU        #
#####################################

def lru():
    espaco_de_memoria = []                                        # Vetor que representa o espaço disponível na memória
    lru_falta_de_pagina = 0                                       # Contador das faltas de página
    lista_de_exclusão = []                                        # Lista para rastrear a página menos usada

    for pagina in paginas:                                        # Passa pelo vetor das páginas
        if pagina not in espaco_de_memoria:                       # Se uma página NÃO está na memória
            if len(espaco_de_memoria) == capacidade:              # Se a memória já está cheia
                vitima = lista_de_exclusão.pop(0)                 # Remove o primeiro elemento da lista de exclusão (o último que foi usado)
                espaco_de_memoria.remove(vitima)                  # Elimina o primeiro elemento do vetor (pop) do espaço de memória

            espaco_de_memoria.append(pagina)                      # Adiciona a página atual no (final) espaço disponível na memória
            lista_de_exclusão.append(pagina)                      # Adiciona a página atual no final da lista de exclusão (representando a mais recente usada)
            lru_falta_de_pagina += 1                              # Incrementa a falta de página

        else:                                                     # Se uma página ESTÁ na memória
            lista_de_exclusão.remove(pagina)                      # Remove a página da lista de exclusão
            lista_de_exclusão.append(pagina)                      # Adiciona a página novamente, porém no final (representando a mais recente usada)

    return lru_falta_de_pagina                                    # Retorna o número de falta de páginas


#####################################
#       IMPLEMENTAÇÃO DO OTM        #
#####################################

def otm():
    espaco_de_memoria = []  
    otm_falta_de_pagina = 0  

    for i, pagina in enumerate(paginas):
        if pagina not in espaco_de_memoria:
            if len(espaco_de_memoria) == capacidade:
                futuras_paginas = paginas[i + 1:]                                             # Cria uma lista a partir do vetor das páginas, que ainda serão chamadas no futuro
                futuras_paginas_unicas = set(futuras_paginas)                                 # Elimina páginas repetidas (set)
                vitimas = [p for p in espaco_de_memoria if p not in futuras_paginas_unicas]   # Aqui é criado um vetor que vai conter as páginas que estão no espaço de memória e que não serão chamdas no futuro
                if not vitimas:
                    vitimas = [p for p in espaco_de_memoria if p in futuras_paginas]          # Pega as páginas que estão na memória e também em paginas_futuras
                espaco_de_memoria.remove(vitimas[0])                                          # Remove apágina escolhida
            espaco_de_memoria.append(pagina)                                                  # Adiciona a página atual
            otm_falta_de_pagina += 1                                                          # Incrementa a falta de página

    return otm_falta_de_pagina

"""
Normalmente, um algoritmo ótimo é uma utopia pois não podemos prever quais páginas serão usadas.
Porém, nesse caso, temos justamente um arquivo contendo as páginas e a ordem que elas aparecem, 
então foi possível implementar essa "previsão". Na vida real, isso não seria possível.                         """


#####################################
#      CHAMANDO OS ALGORITMOS       #
#####################################

print('FIFO: ', fifo())
print('LRU: ', lru())
print('OTM: ', otm())