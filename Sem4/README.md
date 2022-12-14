# Semana 4 - Recursividade :arrows_clockwise:

-- --

## fib_counter.py 

### Enunciado:

> Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:
>
> >0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯
> 
> Após dominar o uso de funções recursivas envolvendo fibonacci, você ficou com uma pergunta na cabeça: "Quantas vezes cada chamada para a função fibonacci é realizada para cada número menor que n
> ?" Para ajudar a responder a essa pergunta, você tentou uma abordagem mais visual que ficou da seguinte forma:
> 
> Perceba que ela começa pelo valor que você deseja calcular (Fibonacci de 4). Essa chamada gera outras duas chamadas para Fibonacci de 2 e 3. A chamada de Fibonacci de 2 gera as chamadas de Fibonacci de 1 e 0 enquanto a chamada de Fibonacci de 3 gera as chamadas de Fibonacci de 2 e 1. Por fim, a chamada de Fibonacci de 2 gera as chamadas de Fibonacci de 1 e 0.
>
> Para não precisar sempre desenhando, o nosso professor mestre das artes marciais pediu a sua ajuda para implementar a um programa que conte quantas vezes cada chamada da função fibonacci(n) é realizada, para cada valor de entrada diferente da função fibonacci(n) é chamada em sua implementação recursiva.

### *Input*

> A entrada consiste de um valor inteiro de 0 ate 30, como por exemplo:
>```
> 5
> ```

### *Output*

> O retorno consiste do valor daquele indice do fibonacci, juntamente com a quantidade de vezes em que cada funçao foi chamada.
> Como por exemplo:
> ``` 
> fibonacci(5) = 5.
> 3 chamada(s) a fibonacci(0).
> 5 chamada(s) a fibonacci(1).
> 3 chamada(s) a fibonacci(2).
> 2 chamada(s) a fibonacci(3).
> 1 chamada(s) a fibonacci(4).
> 1 chamada(s) a fibonacci(5).
> ```

-- --

## sabacchard.py

### Enunciado:

> Na Era Imperial, um dos jogos mais obscuros jogados em Numidian Prime é o Sabacchard, uma variação do jogo de cartas comum Sabacc, aquele em que Lando perdeu a Millennium Falcon. O Sabacchard funciona da seguinte maneira: dada uma sequência de cartas com valores em uma ordem específica, alternadamente o jogador primeiro escolhe uma carta das extremidades para pontuar e, em seguida, escolhe outra carta (também das extremidades) para descartar. O jogador continua com esse processo de pontuar e em seguida descartar, até não haver mais cartas. A pontuação final do jogador é o total de pontos acumulados ao final do processo e se esse valor não é o máximo possível, o jogador perde.
> 
> Assim, Lando pediu sua ajuda para o ajudar a tentar recuperar o prejuízo pela perda da nave, escrevendo um programa para calcular qual a pontuação máxima que o jogador deve alcançar, dada uma distribuição de cartas para o jogo.

### *Input*

> O programa recebe 2 *inputs*, o primeiro contendo o numero de cartas, ja o segundo sendo a sequencia dos valores das cartas separadas por um espaço em branco, como por exemplo:
> ```
> 6
> 7 8 3 4 5 10
> ```

### *Output*

> O retorno esperado e o maior valor cujo pode ser feito a partir dessas cartas.
> Utilizando o *input* acima como exemplo:
> ```
> 25
> ```

-- --

# Codigos extras:

## fib_lerdo.py

> **Aplicaçao "lenta" de *fibonacci*, utilizando recursividade.**

## fib_memo.py

> **Aplicaçao rapida de *fibonacci*, utilizando um metodo chamado de *"memoization"*, onde alocamos os resultados que vao ser
utilizados novamente para o processamento mais rapido da funçao recursiva.**

## fibonacci.py

> **Assim como a aplicaçao acima, utiliza *memoization* para a maior velocidade, porem se utiliza uma aproximaçao comumente 
chamada de *"bottom-up"*, onde nao ha recursao alguma, somente uma logica predefinida, na maioria dos casos.**

## sabacchard_teste.py

> **Versao teste do codigo de [sabacchard.py](#sabacchardpy), onde nao se utiliza da tecnica de *memoization*.**