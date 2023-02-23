# Semana 7 - Grafos :chart_with_upwards_trend:

-- --

## adjacent.py

### Enunciado:

> Um grafo $G=(V,A)$ armazena as informações de um conjunto de vértices e outro de arestas.
> Foi aprendido durante a disciplina que há diferentes formas de se realizar a representação de um grafo e uma delas é a **Matriz de Adjacência**.
> Nessa matriz, dado um grafo $G$ com $n$ vértices, podemos representá-lo em uma matriz $n×n$ onde $A(G)=[a_{ij}]$ (ou simplesmente $A$). A definição precisa 
> das entradas da matriz varia de acordo com as propriedades do grafo que se deseja representar, porém de forma geral o valor $a_{ij}$ guarda informações
> sobre como os vértices $v_i$ e $v_j$ estão relacionados (isto é, informações sobre a adjacência de $v_i$ e $v_j$). Dessa forma, sua tarefa é, dado um grafo 
> com seus respectivos vértices e arestas, imprimir essa representação utilizando uma matriz de adjacências.

### *Input*

**Enunciado:**

> A primeira linha contém dois inteiros e um caracter separados por um espaço, $V (1≤V≤50)$, $E (1≤E≤V^2)$ e $C$, indicando o 
> número de vértices (numeradas de 1 a $V$), o número de arestas e o tipo do grafo, sendo 'D' se o grafo for direcionado e
> 'N' se o grafo for não direcionado. Em seguida, $E$ linhas, cada uma com três inteiros separados por espaços, $X$, $Y$ e $P$, 
> $(1≤X,Y≤N,1≤P≤100)$, indicando que existe uma ligação de $X$ para $Y$ com peso $P$, quando o grafo for direcionado ou uma ligação
> de $X$ para $Y$ e uma ligação de $Y$ para $X$, ambas com peso $P$, quando o grafo for não direcionado.
>
> Por exemplo:
> 
> ```
> 4 6 N
> 3 2 1
> 3 1 1
> 1 4 1
> 2 3 1
> 4 1 1
> 1 3 1
> ```

### *Output*

**Enunciado:**

> A saída deverá conter a respectiva matriz de adjacência $A$, conforme os exemplos abaixo, onde cada peso ocupa 4 espaços ajustado a direita.
>
> Utilizando o *input* anterior, por exemplo:
> 
> ```
>    0   0   1   1
>    0   0   1   0
>    1   1   0   0
>    1   0   0   0
> ```

-- --

## forevis_alone.py

### **Enunciado:**

> O saudoso Mussum seria uma webcelebridade nos dias atuais e, como todo jovem internauta, você gostaria ser amigo dele na rede social. Para isso, precisa solicitar a amizade, portanto tem de chegar a uma relação direta do Trapalhão. Dado um grafo descrevendo as relações da rede social, crie um programa que diga a quantidade mínima de contatos para chegar ao Mussum.

### *Input*

**Enunciado:**

> A primeira linha da entrada indica quantos são os n vértices do grafo (2≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,v1,v2,⋯,vA, onde id é um inteiro identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada vi≠id é um número inteiro identificando um vértice adjacente a id. A última linha apresenta dois ids, separados por espaço, que representam você e Mussum, respectivamente.

### *Output*

**Enunciado:**

>Apresente a quantidade mínima de contatos necessários para chegar ao Mussum, se possível, a mensagem "Forevis alonis..." caso contrário.

-- --

## acaiduto.py

### Enunciado: 

> O Mestre Açaizeiro Bórus Djorus é o responsável pelo novo grande empreendimento da sua cidade: um aqueduto para fornecer açaí a quase todas as residências. Como a tubulação é cara, ele pediu sua ajuda para minimizar os custos e garantir a energia da galera! A sua tarefa é descobrir o menor gasto possível com a tubulação para conectar todas as residências ao fornecedor. Cada metro de tubulação custa R$ 3.14.

### *Input*

**Enunciado:**

>A primeira linha da entrada indica quantos são as n residências da região (1≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,d1,v1,d2,v2,⋯,dA,vA, onde id é um inteiro identificando a residência, A é a quantidade de vizinhos de id, e cada vi≠id é um inteiro identificando uma residência vizinha, que está localizada a uma distância de di metros de id.

### *Output*

**Enunciado:**

> Apresente o valor total da tubulação necessária para ligar todas as residências. 
