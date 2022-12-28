# Semana 5 - Busca e Ordenaçao :mag:

-- --

## study_lesson.py

### Enunciado:

> O professor Zigotto lhe fornece um plano de estudos diário, definindo quais conteúdos você deveria estudar durante o dia. Ciente de sua responsabilidade você sempre completa o plano, estudando pela madrugada para garantir a melhor formação possível.
>
> Para simplificar, cada conteúdo é apresentado como um caractere no plano de estudos e no cronograma do dia, onde você tem acesso ao conteúdo previsto para cada turno de aula (matutino, vespertino e noturno). Planeje suas atividades de meia-noite as seis!

### *Input*

**Enunciado:**

> A primeira linha apresenta um inteiro n indicando a quantidade de testes. Cada teste é composto por quatro linhas, a primeira com o plano de estudos e as seguintes para cada um dos turnos. Todas essas linhas contém uma string com até 100 caracteres de 'A' a 'Z', definindo os conteúdos previstos.
> Como por exemplo:
> ```
> 3
> BANANA
> BANANA
> MACA
> PERA
> CALCULO
> CAL
> O
> LUC
> ABCD
> AB
> 
> C
> ```

### *Output*

**Enunciado:**
> Para cada caso de teste imprima a mensagem "Bora ralar: {conteudo}", com os conteúdos que você estudará na madrugada, em ordem alfabética. Se não houver conteúdo para estudar, chame o Prof. Zigotto para para um projeto de pesquisa com a mensagem "It's in the box!" (ele entenderá o significado). Caso algum professor tenha apresentado conteúdo fora do previsto, avise o Prof. Zigotto com a mensagem "You died!" (ele vai convidá-lo para uma partida de videogame).
> Utilizando o *input* anterior como exemplo:
> ```
> You died!
> It's in the box!
> Bora ralar: D
> ```

-- --

## sort_pretender.py

### Enunciado:

> D. Florinda é trovada por distintos cavalheiros, mas tem certa dificuldade em se lembrar quais lhe agradam mais. Ela é esperta o suficiente para saber que um programa de computador poderia ordená-los conforme suas preferências, facilitando sua vida. Ela também é persuasiva o bastante para lhe convencer a resolver esta tarefa.
>
> D. Florinda adora dançar e por conta disso definiu que a altura ideal para seu parceiro é de 1,80 m. Seu primeiro critério é encontrar alguém que é o mais próximo possível desta altura, não faz diferença ser um pouco mais alto ou mais baixo. Dentre os candidatos, ela prefere alguém o mais próximo possível de 75 kg, pois seus pés dançantes não aceitam alguém mais pesado. Se houver pretendentes da mesma altura, ela escolhe o mais leve (pisões são inevitáveis!). Se dois ou mais candidatos têm as mesmas características físicas, ordene-os pelo sobrenome (e depois pelo primeiro nome se for necessário desempatar).
>
> Defina um algoritmo que ordene uma lista de pretendentes conforme os critérios definidos.

### *Input*

**Enunciado:**
> A entrada consiste em um número n de pretendentes, seguido de n linhas contendo, cada uma, o nome e sobrenome do pretendente (cada um com até 50 caracteres), sua altura (em centímetros - valor inteiro) e sua massa (em quilos - valor inteiro). Os valores são separados por um espaço, e é garantido que não há homônimos e que 2≤n≤100.
> Como por exemplo:
> ```
> 2
> Miguel Rocha 199 138
> Heitor Pereira 200 200
> ```

### *Output*

**Enunciado:**
> A saída deve ser a lista dos pretendentes, um por linha, no formato "Sobrenome, Nome" ordenada conforme as preferências de D. Florinda.
> Utilizando o *input* anterior como exemplo:
> ```
> Rocha, Miguel
> Pereira, Heitor
> ```

-- --

# Codigos extras:

## sort_try.py

> **Versao teste do [sort_pretender.py](#sortpretenderpy).**