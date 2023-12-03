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

#####################################
#       IMPLEMENTAÇÃO DO FIFO       #
#####################################

def fifo():
    espaco_de_memoria = []                                        # Vetor que representa o espaço disponível na memória
    fifo_falta_de_pagina = 0                                      # Contador das faltas de página

    print("\nSimulando FIFO . . . . . . . . . . . . . . . . .")

    for pagina in paginas:                                        # Passa pelo vetor das páginas
        print("-> Acessando página: ", pagina)
        if pagina not in espaco_de_memoria:                       # Se uma página não está na memória
            if len(espaco_de_memoria) == capacidade:              # Se a memória já está cheia
                removida = espaco_de_memoria.pop(0)               # Elimina o primeiro elemento do vetor (pop)
                print("   - Página removida: ", removida)
            espaco_de_memoria.append(pagina)                      # Adiciona a página atual no (final) espaço disponível na memória 
            fifo_falta_de_pagina += 1                             # Incrementa a falta de página
            print("   + Página ", pagina, " adicionada.")
            print("     Memória: ", espaco_de_memoria)
        
        else:
            print("   ! Página já está na memória.")

    return fifo_falta_de_pagina                                   # Retorna o número de falta de páginas


#####################################
#       IMPLEMENTAÇÃO DO LRU        #
#####################################

def lru():
    espaco_de_memoria = []                                        # Vetor que representa o espaço disponível na memória
    lru_falta_de_pagina = 0                                       # Contador das faltas de página
    lista_de_exclusão = []                                        # Lista para rastrear a página menos usada

    print("\nSimulando LRU . . . . . . . . . . . . . . . . .")

    for pagina in paginas:                                        # Passa pelo vetor das páginas
        print("-> Acessando página: ", pagina)
        if pagina not in espaco_de_memoria:                       # Se uma página NÃO está na memória
            if len(espaco_de_memoria) == capacidade:              # Se a memória já está cheia
                vitima = lista_de_exclusão.pop(0)                 # Remove o primeiro elemento da lista de exclusão (o último que foi usado)
                espaco_de_memoria.remove(vitima)                  # Elimina o primeiro elemento do vetor (pop) do espaço de memória
                print("   - Página removida: ", vitima)

            espaco_de_memoria.append(pagina)                      # Adiciona a página atual no (final) espaço disponível na memória
            lista_de_exclusão.append(pagina)                      # Adiciona a página atual no final da lista de exclusão (representando a mais recente usada)
            lru_falta_de_pagina += 1                              # Incrementa a falta de página
            print("   + Página ", pagina, " adicionada.")
            print("     Memória: ", espaco_de_memoria)

        else:                                                     # Se uma página ESTÁ na memória
            lista_de_exclusão.remove(pagina)                      # Remove a página da lista de exclusão
            lista_de_exclusão.append(pagina)                      # Adiciona a página novamente, porém no final (representando a mais recente usada)
            print("   ! Página já está na memória.")

    return lru_falta_de_pagina                                    # Retorna o número de falta de páginas


#####################################
#       IMPLEMENTAÇÃO DO OTM        #
#####################################

def otm():
    espaco_de_memoria = []                                                                    # Vetor que representa o espaço disponível na memória
    otm_falta_de_pagina = 0                                                                   # Contador das faltas de página

    print("\nSimulando OTM . . . . . . . . . . . . . . . . .")

    for i, pagina in enumerate(paginas):
        if pagina not in espaco_de_memoria:
            print("-> Acessando página: ", pagina)
            if len(espaco_de_memoria) == capacidade:
                futuras_paginas = paginas[i + 1:]                                             # Cria uma lista a partir do vetor das páginas, que ainda serão chamadas no futuro
                futuras_paginas_unicas = set(futuras_paginas)                                 # Elimina páginas repetidas (set)
                vitimas = [p for p in espaco_de_memoria if p not in futuras_paginas_unicas]   # Aqui é criado um vetor que vai conter as páginas que estão no espaço de memória e que não serão chamdas no futuro
                if not vitimas:
                    vitimas = [p for p in espaco_de_memoria if p in futuras_paginas]          # Pega as páginas que estão na memória e também em paginas_futuras
                espaco_de_memoria.remove(vitimas[0])                                          # Remove apágina escolhida
                print("   - Página removida: ", vitimas[0])
            espaco_de_memoria.append(pagina)                                                  # Adiciona a página atual
            otm_falta_de_pagina += 1                                                          # Incrementa a falta de página
            print("   + Página ", pagina, " adicionada.")
            print("     Memória: ", espaco_de_memoria)

        else:
           print("   ! Página já está na memória.") 

    return otm_falta_de_pagina                                                                # Retorna o número de falta de páginas

"""
Normalmente, um algoritmo ótimo é uma utopia pois não podemos prever quais páginas serão usadas.
Porém, nesse caso, temos justamente um arquivo contendo as páginas e a ordem que elas aparecem, 
então foi possível implementar essa "previsão". Na vida real, isso não seria possível.                         """


#####################################
# CHAMANDO E ORGANIZANDO A LEITURA  #
#####################################

arquivo = 'arquivo.txt'                                           # Diz qual o arquivo
linhas = ler_arquivo(arquivo)                                     # Chama a função pra ler o arquivo

if linhas is not None:                                            # Se o arquivo tiver sido encontrado
    capacidade = int(linhas[0])                                   # Pega a primeira linha
    paginas = [int(pagina) for pagina in linhas[1:]]              # Cria um vetor com as outras linhas ([1:] = índice 1 pra frente)


#####################################
#      CHAMANDO OS ALGORITMOS       #
#####################################

print('\n--> FIFO: ', fifo(), '\n\n')
print('\n--> LRU: ' , lru() , '\n\n')
print('\n--> OTM: ' , otm() , '\n\n')
