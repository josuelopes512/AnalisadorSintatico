# AnalisadorSintatico

O analisador sintático preditivo de descendência recursiva é um dos mais simples para se
implementar à mão. Ele usa funções recursivas associadas a gramática. Tais funções são: Cabeça,
Último, Primeiro(First) e Seguinte (Follow).
Realize a implementação da função First

Primeiro foi definido 2 vetores separando dos simbolos terminais do não terminais
Depois Foi Definido um Vetor para armazenar a Gramatica, separando as regras gramaticais
Depois baseado nos vetores representando as regras gramaticais de reprodução, os simbolos terminais e não terminais
foi implementado o algoritmo first, que detecta o primeiro simbolo terminal de uma regra gramatical que começam
qualquer seqüência derivável.
Depois foi feita uma tabela representativa dos primeiros dos simbolos não terminais


<img src=https://i.imgur.com/hmn3t5G.png/>

<img src=https://i.imgur.com/CS2LT8y.png/>
