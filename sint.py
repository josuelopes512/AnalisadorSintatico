# -*- coding: utf-8 -*-
from grammar import Grammar
import re

def transform2(string,lista):
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
    first = {i: set() for i in grammar.nonterminals}
    first.update((i, {i}) for i in grammar.terminals)
    follow = {i: set() for i in grammar.nonterminals}

    lista = sorted((list(grammar.terminals)+list(grammar.nonterminals)), key=len, reverse=True)
    rule = tuple([(i, transform2(j, lista)) for i, j in grammar.rules])
    
    # epsilon = {'ε'}
    epsilon = set()

    while True:
        updated = False
        for nt, expression in rule:
            for symbol in expression:
                updated |= union(first[nt], first[symbol])
                if symbol not in epsilon:
                    break
                else:
                    updated |= union(epsilon, {nt})

            aux = follow[nt]
            for symbol in reversed(expression):
                if symbol in follow:
                    updated |= union(follow[symbol], aux)
                if symbol in epsilon:
                    aux = aux.union(first[symbol])
                else:
                    aux = first[symbol]        
        if not updated:
            # epsilon = {'ε'}
            return first, follow, epsilon

def First(grammar):
    first = {i: set() for i in grammar.nonterminals}
    first.update((i, {i}) for i in grammar.terminals)

    lista = sorted((list(grammar.terminals)+list(grammar.nonterminals)), key=len, reverse=True)
    rule = tuple([(i, transform2(j, lista)) for i, j in grammar.rules])
    

    epsilon = {'ε'}

    while True:
        updated = False
        for nt, expression in rule:
            for symbol in expression:
                updated |= union(first[nt], first[symbol])
                if symbol not in epsilon:
                    break
                else:
                    updated |= union(epsilon, {nt})
        
        if not updated:
            epsilon = {'ε'}
            return first, epsilon

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
        # print(a)
        for i in first:
            a = "Primeiro({}) = {}".format(i, first[i])
            file.write(a + '\n')
            # print(a)
    print("\n")
    with open('Follow.txt', 'w+', encoding="utf-8") as file:
        a = "Epsilon = {}".format(epsilon)
        file.write(a + '\n')
        # print(a)
        for i in follow:
            a = "Follow({}) = {}".format(i, follow[i])
            file.write(a + '\n')
            # print(a)


def printArquivo(dir):
    with open(dir, "r", encoding="utf-8") as file:
        for line in file:
            print(line)

def visualizar_gr(lista):
    for i in lista:
        print(i)

def main():
    dir = "gramaticas"
    gramatica = [f'{dir}/a.txt', f'{dir}/b.txt', f'{dir}/c.txt']
    escolha = int(input('1 - a.txt\n2 - b.txt\n3 - c.txt\n\nEscolha uma Gramatica: '))
    caminho = gramatica[escolha-1]
    gr = lerArquivo(caminho) #"gramaticas/a.txt"
    visualizar_gr(gr)
    a = Grammar(gr)

    first, follow, epsilon = FirstAndFollow(a)
    gravarArquivo(first, follow, epsilon)
    print('-----------------------------------------------------------------')
    print("1 - Visualizar First\n2 - Visualizar Follow\n3 - Visualizar First e Follow")
    X = True
    while X:
        op = input('\nDigite a Opção: ')
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


# S -> AB
# A -> aA | a 
# A -> ε
# B -> bB | c 
# B -> ε

# E -> TE'
# E' -> +TE' | ε
# T -> FT'
# T' -> *FT' | ε
# F -> (E) | id

# S -> aABb $
# A -> c | ε
# B -> d | ε