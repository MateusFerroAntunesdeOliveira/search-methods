## Search Methods - Problema do Duende Perdido

#### Projeto está sendo desenvolvido na Linguagem Python - disciplina de Inteligência Artificial e Computacional (AIC) da Pontifícia Universidade Católica do Paraná (PUC-PR)

#### Implementação: Blind (breadth and depth) and heuristic (with A*) search methods
----------------------
#### @MateusFerroAntunesdeOliveira @ijoaog @GabrielSkf
* Work Done - 29/08/2022

----------------------
### Como utilizar:
Rode, na respectiva pasta do projeto (onde está o arquivo 'main.py'):

```
  python main.py content/duende_2.csv
```

<p align="justify">
<b> Observação importante:</b> Deve haver uma pasta 'content' com um arquivo chamado duende.csv para o programa conseguir interpretar o mapa do problema
</p>

----------------------
### Descrição:

<p align="justify">
  Gugo, o duende, ficou preso em uma caverna e precisa sair o mais rapidamente possível. A caverna é formada por salões interligados por túneis, na forma de uma grade retangular, com N linhas e M colunas. Alguns dos salões da caverna têm paredes de cristal. Duendes, como todos sabem, não gostam de ficar em ambientes com qualquer tipo de cristal, pois seus organismos entram em ressonância com a estrutura de cristais, e em casos extremos os duendes podem até mesmo explodir. Compreensivelmente, Gugo não quer entrar em nenhum salão com parede de cristal.
</p>

<p align="justify">
  A figura abaixo mostra uma caverna com quatro linhas e cinco colunas de salões; os salões cinza têm paredes de cristal. A posição inicial de Gugo é indicada com um caractere ‘*’.
</p>

![image](https://user-images.githubusercontent.com/53230135/186498760-8ef34947-6da0-46cb-9077-21b8a4a94959.png)

<h3> Tarefa: </h3>
<p align="justify">
  Você deve escrever um programa que, dadas a configuração da caverna e a posição inicial de Gugo dentro da caverna, calcule qual o número mínimo de salões pelos quais o duende deve passar antes de sair da caverna (não contando o salão em que o duende está inicialmente), mas contando o salão que tem saída para o exterior).
</p>

<h3> Entrada: </h3>
<p align="justify">
  A caverna será modelada como uma matriz de duas dimensões, cujos elementos representam os salões. Um salão que não tem parede de cristal e que tem saída para o exterior da caverna é representado pelo valor 0; um salão que não tem parede de cristal e não tem saída para o exterior é representado pelo valor 1; um salão que tem parede de cristal é representado pelo valor 2; e o salão em que o duende está inicialmente (que não tem saída para o exterior e nem paredes de cristal) é representado pelo valor 3. A figura abaixo mostra a representação da caverna apresentada acima.
</p>

![image](https://user-images.githubusercontent.com/53230135/186499936-b79b3946-b965-45bd-8552-45f684fd70c2.png)

<p align="justify">
  A primeira linha da entrada contém dois números inteiros N e M que indicam respectivamente o número de linhas (1 <= N <= 10) e o número de colunas (1 <= M <= 10) da representação da caverna. Cada uma das N linhas seguintes contém M números inteiros Ci, descrevendo os salões da caverna e a posição inicial do duende (0 <= Ci <= 3). Você pode supor que sempre há um trajeto que leva Gugo à saída da caverna.
</p>

<h3> Saída: </h3>
<p align="justify">
  Seu programa deve produzir uma unica linha na saída, contendo um número inteiro representando a quantidade mínima de salões pelos quais Gugo deve passar antes de conseguir sair da caverna (não contando o salão em que ele está inicialmente, mas contando o salão que tem saída para o exterior).
</p>


<h3> Exemplo: </h3>

```
  Entrada:
  4,5
  0,1,1,1,1
  0,2,2,2,1
  2,1,1,1,1
  1,1,1,3,1
  
  Saída
  8
```
ou

```
  Entrada:
  8,10
  1,1,1,1,1,3,2,2,2,2
  1,2,2,2,2,1,2,2,2,2
  1,2,2,2,2,1,2,2,2,2
  1,1,1,2,2,1,1,1,2,2
  1,2,1,2,2,2,2,1,2,2
  1,2,1,1,1,1,1,1,2,2
  1,2,2,2,2,2,2,2,2,2
  0,2,2,2,2,2,2,2,2,2
```
