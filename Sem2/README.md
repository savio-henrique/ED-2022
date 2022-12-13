# Semana 2 - Pilha e Fila :green_book:

-- --

## gym_weights.py

**O programa retira anilhas de uma barra (*pilha*).**

### *Input*

> O programa recebe *n* *inputs*, sendo esses os valores dos pesos das anilhas, ate receber o valor **0**.
> Em diante, ele recebe o peso da anilha que quer que retire.
> Como por exemplo:
>> * 20
>> * 15
>> * 10
>> * 2
>> * 8
>> * 0 ***(Ponto de parada)***
>> * 15 ***(Anilha a ser retirada)***

### *Output*

> E aguardado o retorno sendo ***'valor'*** a anilha retirada, ***'qtd'*** a quantidade de anilhas 
> movidas ao retirar e ***'soma'*** a soma dos pesos das anilhas movidas:
>> * Peso retirado: ***'valor'***
>> * Peso retirado: ***'valor'***
>> * Anilhas retiradas: ***'qtd'*** ***(nesse caso seria 2)***
>> * Peso total movimentado: ***'soma'***

-- --
## priorities_queue.py

**O programa separa e organiza uma certa quantidade de atividades por sua respectiva prioridade e 
retira a quantidade pedida.**

### *Input*

> O programa recebe 2 *inputs*, o primeiro sendo as atividades seguidas de suas respectivas prioridades, as mesmas 
> separadas por um espaço em branco. Ja o segundo e a quantidade de atividades a serem feitas, assim as retirando 
> da fila de prioridade.
> Como por exemplo:
>> * estudar 1 comer 3 dormir 1 jogar 3 ***(primeiro input)***
>> * 2 ***(segundo input)***

### *Output*

> O retorno se da pelo tamanho da fila e a fila em si. Como por exemplo, utilizando o exemplo de input anterior:
>> * Tamanho da fila: 2
>> * Atividade: comer, Prioridade: #3
>> * Atividade: jogar, Prioridade: #3

> ***Obs.:*** **A fila tem de ser organizada pela prioridade seguindo a ordem de apariçao quando 
> conflitar a prioridade de duas atividades**

-- --

### priorities_queue_only_queue.py

#### O mesmo programa que o anterior, porem utilizando somente a estrutura da fila, sem uso de dicionarios.
*(em progresso)*