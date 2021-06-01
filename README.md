# Analisador Sintático 
	
## Aplicação do Algoritmo First e Follow

	O analisador sintático preditivo de descendência recursiva é um dos mais simples para se
	implementar à mão. Ele usa funções recursivas associadas a gramática. Tais funções são: Cabeça,
	Último, Primeiro(First) e Seguinte (Follow).
	Realize a implementação da função First
	
	Primeiro foi definido 2 vetores separando dos simbolos terminais do não terminais
	Depois Foi Definido um Vetor para armazenar a Gramatica, separando as regras gramaticais
	Depois baseado nos vetores representando as regras gramaticais de reprodução, 
	os simbolos terminais e não terminais foi implementado o algoritmo first, que detecta o 
	primeiro simbolo terminal de uma regra gramatical que começam qualquer seqüência derivável.
	Depois foi feita uma tabela representativa dos primeiros dos simbolos não terminais

<img src=https://i.imgur.com/hmn3t5G.png/>

<img src=https://i.imgur.com/B5lxGbc.png/>


### Dada a gramática G

	G = (Vn, Vt, P, S)
	Vn = E, E', T, T', F
	Vt = id, + , ε , * , (, )
	ε = Épsilon

	E -> TE'
	E' -> +TE' | ε
	T -> FT'
	T' -> *FT' | ε
	F -> (E) | id

<img src=https://i.imgur.com/CS2LT8y.png/>


	OBS: Esse Projeto Foi Implementado utilizando Python e Desenvolvido no VSCODE
	para executar o projeto não abra o projeto em subpasta. 
	Abra o projeto "Abrir Pasta" no vscode e selecione a pasta "AnalisadorSintatico-01-06"
	Para executar python3 main.py
