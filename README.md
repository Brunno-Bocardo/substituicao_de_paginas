# Algoritmo de Substituição de Páginas

O objetivo deste projeto é escrever um programa para simular os principais algoritmos de substituição de páginas usados no gerenciamento da memória virtual.
- FIFO (First In, First Out)
- OPT (Algoritmo ótimo)
- LRU (Least Recently Used)

A saída esperada para esse projeto é a quantidade de falta de páginas que cada algorítimo apresentou, algo como:
- FIFO: 9
- LRU: 8
- OTM: 7


## Setup:
Para rodar o projeto, deve-se ter intalado o Python em sua máquina. Depois disso, basta executar o arquivo main.py em um editor de código, como O Visual Studio.

## Arquivos:
O projeto possui 2 arquivos.
- main.py: arquivo que contém os 3 tipos de algoritmo. Ele faz a leitura e processamento do outro arquivo
- arquivo.txt: arquivo que simula as páginas e ordem com que as páginas entram. Além disso, o número contido na primeira linha representa a quantidade de espaço disponível na memória (como uma simulação)

## Pílula de Conhecimento:

### O que é uma página?
Página é uma unidade de alocação de memória, com um tamanho fixo de (geralmente) 4 KB. As páginas são usadas para dividir memória (física e virtual) em pedaços gerenciáveis. Esses pedaços são usados como unidade de transferência de dados entre a memória física (RAM) e virtual (disco), facilitando a alocação e o gerenciamento de memória, já que a cópia de páginas inteiras é mais eficiente do que manipular pequenos pedaços de dados. 

### Como é feita a substituição?
Quando um novo acesso à memória é solicitado e não há espaço disponível nos quadros da memória física, é necessário escolher uma página para ser substituída. Isso é o que os algoritmos de substituição de páginas fazem. Eles selecionam a página a ser substituída com base em suas políticas específicas (FIFO, LRU, OPT, etc.), removendo-a da memória e carregando a nova página no espaço vago.

### FIFO:
Basicamente o algoritmo FIFO é uma fila. O primeiro que entra é o primeiro que sai. Ele funciona da seguinte forma: quando é necessário carregar uma página na memória física, a página mais antiga que está na memória é a primeira a ser removida (a que entrou primeiro).

### LRU:
O algoritmo LRU substitui a página que não era usada há mais tempo. Ele mantém um registro do histórico de acesso das páginas e remove aquela que foi acessada menos recentemente. Isso é feito com base no princípio de que páginas que não foram usadas recentemente provavelmente não serão usadas no futuro próximo.

### OTM:
É um algoritmo que resolve o problema com o mínimo de recursos possíveis. O algoritmo ótimo é um algoritmo ideal, mas teoricamente impossível de implementar na prática. Ele substitui a página que não será usada por mais tempo no futuro. Isso requer prever qual página não será referenciada por mais tempo, o que é difícil de fazer na prática. O algoritmo OPT serve como um ponto de referência para comparar o desempenho de outros algoritmos. Nesse projeto, apenas foi possível simular esse algoritmo pois já tinhamos uma lista de quais seriam as próximas páginas a entrarem, tornando possível a "previsão".
