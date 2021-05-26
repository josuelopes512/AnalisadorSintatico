# -*- coding: utf-8 -*-
#! /usr/bin/python3

from grammar import Grammar
import re

def transform2(string,lista): # conversão e filtragem
    listanova=[]
    texto=""
    tam=len(string)
    x = 0
    while x < tam:
        texto +=string[x]
        if(x < tam-1 and texto+string[x+1] in lista):
            listanova.append(texto+string[x+1])
            texto=""
            x +=1
        elif texto in lista: 
            listanova.append(texto)
            texto=""
        x+=1
    return listanova

def FirstAndFollow(grammar):
    first = {i: set() for i in grammar.nonterminals} # Conjunto de inicio do First
    first.update((i, {i}) for i in grammar.terminals) 
    follow = {i: set() for i in grammar.nonterminals} # Conjunto de inicio do Follow
    # print(first)
    # print(follow)

    # lista dos terminais e não terminais
    lista = sorted((list(grammar.terminals)+list(grammar.nonterminals)), key=len, reverse=True)
    
    # regras gramaticais separados por tuplas (Não terminais, expressões)
    rule = tuple([(i, transform2(j, lista)) for i, j in grammar.rules])
    
    #Determina o simbolo do Epsilon
    epsilon = {'ε'}

    # Algoritmo Não Recursivo
    # O loop de parada 
    # Quando acaba de processar todas as expressões 
    # e ponto de retorno da função
    # quando o updated for True

    while True:
        #
        updated = False
        for nt, expression in rule: #Processa expressão por expressão por vez

            # Logica que Calcula o First da Expressão
            # Identifica em quais expressões está o epsilon
            # e armazena o simbolo não terminal correspondente
            # a expressão no conjunto Epsilon
            for symbol in expression:
                updated |= union(first[nt], first[symbol])
                if symbol not in epsilon:
                    break
                else:
                    updated |= union(epsilon, {nt})

            #Logica que Calcula o Follow da Expressão
            aux = follow[nt]
            for symbol in reversed(expression):
                if symbol in follow:
                    updated |= union(follow[symbol], aux)
                if symbol in epsilon:

                    # União do conjunto first[symbol] com o 
                    # conjunto auxiliar anterior 
                    # formando um novo auxiliar
                    aux = aux.union(first[symbol])
                else:
                    aux = first[symbol]

        if not updated:
            for chave, valor in follow.items():
                if 'ε' in follow[chave]:
                    follow[chave] = follow[chave] - {'ε'}

            cond1 = False
            cond2 = False
            for i in epsilon:
                if '^' in i:
                    cond1 = True
                if 'ε' in i:
                    cond2 = True

            for i in grammar.nonterminals:
                if '^' in i:
                    first.pop(i)
                    follow.pop(i)
                if cond1 and '^' in i:
                    epsilon.remove(i)

            for i in grammar.terminals:
                first.pop(i)
                if cond2 and 'ε' in i:
                    epsilon.remove(i)
                    
            return first, follow, epsilon


# calcula o tamanho do conjunto first
# une o conjunto first atual com o conjunto Begins
# forma-se um novo conjunto first
# e calcula se o tamanho do conjunto do first atual  
# é diferente do tamanho do conjunto first anterior
# se for diferente retorna-se True
# senão retorna-se False
def union(first, begins):
    n = len(first)
    first |= begins
    return len(first) != n

def tratarArq(lista): # trata lista e converte
    lista = " ".join(lista.split())
    lista = re.split(r' ', lista)
    return lista

def lerArquivo(dir):
    arquivo = []
    b = []
    inicio = ""
    fim = ""
    
    with open(dir, "r") as gramatica:
        for line in gramatica:
            arquivo.append(line.replace('Îµ', 'ε').strip().split('\n'))
    arquivo = [i for j in arquivo for i in j]

    for i in range(0, len(arquivo)):
        temp = []
        temp = tratarArq(arquivo[i])
        arquivo[i] = temp
             
    for i in range(0, len(arquivo)):
        tam = len(arquivo[i])
        for j in range(0, tam):    
            if "|" in arquivo[i][j]:
                inicio = arquivo[i][0]+" "+arquivo[i][1]
                fim = arquivo[i][-1]
                suma = inicio+" "+fim
                arquivo.append(tratarArq(suma))
    
    for i in arquivo:
        b.append(" ".join(i[:3]))
    return b

def gravarArquivo(first, follow, epsilon):
    with open('First.txt', 'w+', encoding="utf-8") as file:
        a = "Epsilon = {}".format(epsilon)
        file.write(a + '\n')
        for i in first:
            a = "Primeiro({}) = {}".format(i, first[i])
            file.write(a + '\n')
    print("\n")
    with open('Follow.txt', 'w+', encoding="utf-8") as file:
        a = ''
        for i in follow:
            a = "Follow({}) = {}".format(i, follow[i])
            file.write(a + '\n')

def printArquivo(dir):
    with open(dir, "r", encoding="utf-8") as file:
        for line in file:
            print(line)

def visualizar_gr(lista):
    for i in lista:
        print(i)

def main():
    dir = "gramaticas"
    gramatica = [dir+'/a.txt', dir+'/b.txt', dir+'/c.txt', dir+'/d.txt', dir+'/e.txt', dir+'/f.txt', dir+'/g.txt']
    escolha = int(input('1 - a.txt\n2 - b.txt\n3 - c.txt\n4 - d.txt\n5 - e.txt\n6 - f.txt\n7 - g.txt\n\nEscolha uma Gramatica: '))
    caminho = gramatica[escolha-1]
    gr = lerArquivo(caminho)
    visualizar_gr(gr)
    a = Grammar(gr)

    first, follow, epsilon = FirstAndFollow(a)
    gravarArquivo(first, follow, epsilon)
    print('-----------------------------------------------------------------')
    X = True
    while X:
        op = input('1 - Visualizar First\n2 - Visualizar Follow\n3 - Visualizar First e Follow\n\nDigite a Opção: ')
        print('\n---------------------------------------------------------------------\n')
        if op == '1':
            printArquivo('First.txt')
            X = False
        if op == '2':
            printArquivo('Follow.txt')
            X = False
        if op == '3':
            printArquivo('First.txt')
            print('-----------------------------------------------------------------\n')
            printArquivo('Follow.txt')
            X = False
main()