def transform2(string, lista):  # conversão e filtragem
    listanova = []
    texto = ""
    tam = len(string)
    x = 0
    while x < tam:
        texto += string[x]
        if(x < tam-1 and texto+string[x+1] in lista):
            listanova.append(texto+string[x+1])
            texto = ""
            x += 1
        elif texto in lista:
            listanova.append(texto)
            texto = ""
        x += 1
    return listanova

def tr3(string, lista):  # conversão e filtragem
    stringnova = ""
    tam = len(string)
    x = 0
    while x < tam:
        if(x < tam-1 and str(string[x]) + str(string[x+1]) in lista):
            stringnova += str(" ")+str(string[x])+str(string[x+1])+str(" ")
            x += 1
        elif(str(string[x]) in lista):
            stringnova += " "+str(string[x])+" "
        else:
            stringnova += str(string[x])
        x += 1
    return list(filter(lambda x: x != "", stringnova.split(" ")))

def FirstAndFollow(terminais, nao_terminais, regras):
    # lista dos terminais e não terminais
    lista = sorted((list(terminais)+list(nao_terminais)),
                   key=len, reverse=True)

    first = {i: set() for i in nao_terminais} # Conjunto de inicio do First
    first.update((i, {i}) for i in terminais)
    follow = {i: set() for i in nao_terminais} # Conjunto de inicio do Follow


    # regras gramaticais separados por tuplas (Não terminais, expressões)
    rule = tuple([(i, transform2(j, lista)) for i, j in regras])

    if not ('^' in rule[0][0]):
        rule = [list(i) for i in rule]
        valor = [rule[0][0], '$']
        rule.insert(0, ['^', valor])
        lista = sorted((list(lista) + list('$') + list('^')),
                       key=len, reverse=True)
        terminais |= {'$'}
        nao_terminais |= {'^'}
        rule = tuple(tuple(i) for i in rule)
        first = {i: set() for i in nao_terminais}
        first.update((i, {i}) for i in terminais)
        follow = {i: set() for i in nao_terminais}

    #Determina o simbolo do Epsilon
    epsilon = {'ε'}

    # Algoritmo Não Recursivo
    # O loop de parada 
    # Quando acaba de processar todas as expressões 
    # e ponto de retorno da função
    # quando o updated for True

    while True:
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

            for i in nao_terminais:
                if '^' in i:
                    first.pop(i)
                    follow.pop(i)
                if cond1 and '^' in i:
                    epsilon.remove(i)

            for i in terminais:
                # first.pop(i)
                first['$'] = '$'
                if cond2 and 'ε' in i:
                    epsilon.remove(i)
            for i in {'$'}:
                first.pop(i)

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