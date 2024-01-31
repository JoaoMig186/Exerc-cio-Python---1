# Exercícios Python
Estes são exercícios que foram utilizados como avaliação na minha faculdade na graduação de Engenharia de Software na matéria de Lógica, Computação e Algoritmos.

Todos os enunciados das questões estão nas primeiras linhas dos códigos.

1 -Na pasta "Verificação de renda" (que corresponde à questão 3), temos um código que pede como entrada a sua renda mensal e seus gastos com moradia, educação e transporte. Ele calcula as porcentagens dos gastos de acordo com a sua renda e diz se você é saudável financeiramente ou não.
O enunciado do exercício está nas primeiras linhas do código.

2 - Na pasta "Cálculo de rendimento de dinheiro" (que corresponde à questão 4), temos um código que pede como entrada um valor inicial que você tenha, a porcentagem dos juros que vair render por período, um aporte que você recebe por período e a quantidade de períodos. Ele irá calcular quantos reais você receberá a cada período, passando pelo cálculo dos juros e da soma do aporte.
O enunciado do exercício está nas primeiras linhas do código.

3- Na pasta "PIB's" (que corresponde à questão 5), temos um código que lê uma tabela EXCEL .csv (tabelaPIBs.csv) contendo os PIB's de alguns países em um período de 2013 a 2020. Ele funciona como um programa que dá 4 opções ao usuário: 

 - Questão (A), onde o usuário entra com o nome do país e o ano em que ele deseja ver o PIB. Logo após isso, a saída mostrará o PIB do país que foi digitado;
 - Questão (B), onde o usuário entra com o nome do país que deseja ver a variação do PIB. Logo após isso, a saída mostrará a variação do PIB de acordo com o país digitado;
 - Questão (C), onde o usuário entra com o nome do país que deseja ver o gráfico dos PIBs com o passar dos anos. Logo após isso, será exibido o gráfico do país selecionado;
 - Sair do programa, onde o usuário entra digitando 0 e após a confirmação, o programa se encerra.

Foi usada a biblioteca Pandas do Python para usar os métodos de dataFrame para manipular os dados da tabela. O código conta com uma falha: Não há tratamento de exceção caso o usuário passe um ano que não está na tabela. O programa apresentará um erro ou se encerrará. 
O enunciado do exercício está nas primeiras linhas do código.

