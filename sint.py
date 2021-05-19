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

def First(grammar):
    first = {i: set() for i in grammar.nonterminals}
    first.update((i, {i}) for i in grammar.terminals)

    lista = sorted((list(grammar.terminals)+list(grammar.nonterminals)), key=len, reverse=True)
    rule = tuple([(i, transform2(j, lista)) for i, j in grammar.rules])

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
        
        if not updated:
            epsilon = {'ε'}
            for i in first:
                if first[i] == set():
                    first[i] = {'ε'} 
            return first, epsilon

def union(first, begins):
    n = len(first)
    first |= begins
    return len(first) != n

def tratarArq(lista): # trata lista e converte
    lista = " ".join(lista.split())
    lista = re.split(r' ', lista)
    return lista

def lerArquivo():
    arquivo = []
    b = []
    inicio = ""
    fim = ""
    
    with open("gramatica.txt", "r") as gramatica:
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

def main():
    gr = lerArquivo()
    a = Grammar(gr)
    first, epsilon = First(a)
    print("Epsilon =",epsilon)
    for i in first:
        print("Primeiro({})".format(i),"=", first[i])

main()