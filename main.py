# -*- coding: utf-8 -*-
#! /usr/bin/python3

import re
from pathlib import Path
from os import system, name
from grammar import Grammar
from funcoes import FirstAndFollow

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

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
    outpath = 'output'
    Path(outpath).mkdir(exist_ok=True)
    with open(outpath+'/First.txt', 'w+', encoding="utf-8") as file:
        a = "Epsilon na Gramatica = {}".format(epsilon)
        file.write(a + '\n')
        for i in first:
            a = "Primeiro({}) = {}".format(i, first[i])
            file.write(a + '\n')
    print("\n")
    with open(outpath+'/Follow.txt', 'w+', encoding="utf-8") as file:
        a = ''
        for i in follow:
            a = "Follow({}) = {}".format(i, follow[i])
            file.write(a + '\n')

def printArquivo(dir):
    with open(dir, "r", encoding="utf-8") as file:
        for line in file:
            print(line)

def limpar_terminais_first(terminais, first):
    for i in terminais - {'$'}:
      first.pop(i)

def visualizar_saida():
    print('-----------------------------------------------------------------')
    X = True
    while X:
        op = input('1 - Visualizar First\n2 - Visualizar Follow\n3 - Visualizar First e Follow\n\nDigite a Opção: ')
        print('\n---------------------------------------------------------------------\n')
        if op == '1':
            clear()
            printArquivo('output/First.txt')
            X = False
        if op == '2':
            clear()
            printArquivo('output/Follow.txt')
            X = False
        if op == '3':
            clear()
            printArquivo('output/First.txt')
            print('-----------------------------------------------------------------\n')
            printArquivo('output/Follow.txt')
            X = False


def visualizar_gr(lista):
    for i in lista:
        print(i)


def comentarios_sobre_gramaticas(escolha):
    if escolha == 1:
        print("Sobre a Gramatica a.txt, é necessário (((comentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")
    if escolha == 2:
        print("Sobre a Gramatica b.txt, é necessário (((descomentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")
    if escolha == 3:
        print("Sobre a Gramatica c.txt, é necessário (((descomentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")
    if escolha == 4:
        print("Sobre a Gramatica d.txt, é necessário (((descomentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")
    if escolha == 5:
        print("Sobre a Gramatica e.txt, é necessário (((descomentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")
    if escolha == 6:
        print("Sobre a Gramatica f.txt, é necessário (((descomentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")
    if escolha == 7:
        print("Sobre a Gramatica g.txt, é necessário (((descomentar))) \na penuntima linha da Função 'terminals' \nLocalizada em grammar.py Dentro da Classe Grammar \npara um bom funcionamento do código")


def main():
    dir = "gramaticas"

    gramatica = [dir+'/a.txt', dir+'/b.txt', dir+'/c.txt', dir+'/d.txt', dir+'/e.txt', dir+'/f.txt', dir+'/g.txt']
    
    clear()
    print("Selecione Entre 1 até 9:\n")
    print("1 - a.txt\n2 - b.txt\n3 - c.txt\n4 - d.txt\n5 - e.txt\n6 - f.txt\n7 - g.txt\n8 - h.txt\n9 - i.txt\n\n")
    escolha = int(input('Escolha uma Gramatica: '))

    if not (escolha in [i for i in range(1, 10)]):
        print("Escolha Invalida")
        exit()
    
    clear()

    comentarios_sobre_gramaticas(escolha)
    confirmar = input("Digite OK para Continuar ou qualquer coisa para finalizar: ")
    if confirmar != 'OK':
        clear()
        exit()
    elif confirmar == 'OK':
        pass
    
    clear()

    gr = lerArquivo(gramatica[escolha-1])

    visualizar_gr(gr)

    gramatica = Grammar(gr)

    terminais, nao_terminais, regras = gramatica.terminals, gramatica.nonterminals, gramatica.rules

    first, follow, epsilon = FirstAndFollow(terminais, nao_terminais, regras)

    limpar_terminais_first(terminais, first)

    gravarArquivo(first, follow, epsilon)

    visualizar_saida()

if __name__ == "__main__":
    main()