import re

def tr3(string, lista):
    stringnova=""
    tam=len(string)
    x=0
    while x<tam:
        if(x<tam-1 and str(string[x]) + str(string[x+1]) in lista):
            stringnova+= str(" ")+str(string[x])+str(string[x+1])+str(" ")
            x+=1
        elif(str(string[x]) in lista):
            stringnova+=" "+str(string[x])+" "
        else:
            stringnova+=str(string[x])
        x+=1
    return list(filter(lambda x:x!="",stringnova.split(" ")))

class Grammar:
    def __init__(self, rules):
        rules = tuple(rules)
        self.rules = tuple(self._parse(rule) for rule in rules)

    def _parse(self, rule):
        return tuple(rule.replace(' ', '').split('->'))
        
    def __getitem__(self, nonterminal):
        yield from [rule for rule in self.rules if rule[0] == nonterminal]
        
    @staticmethod 
    def is_nonterminal(symbol):
        return symbol.isalpha() and symbol.isupper()

    @property
    def nonterminals(self):
        return set([nt for nt, _ in self.rules])
        
    @property
    def terminals(self):       
        a = [
            expression
            for _, expression in self.rules
            if not self.is_nonterminal(expression)
        ]
        
        nt = sorted([nt for nt, _ in self.rules], key=len, reverse=True)
        a = [i for j in [tr3(i, nt) for i in a] for i in j]
        
        # print(a)

        for i in nt: #mudar aqui aABb expressao regular
            for j in range(0, len(a)):
                if re.search(i, a[j]):
                    a[j] = a[j].replace(i, '')
                a[j] = " ".join(a[j].split())
        # print(a)
        
        tmp = []  
        for i in a:
            if i != '' and i not in tmp:
                tmp.append(i)
        a = tmp
        # print(a)
        tmp = []
        for i in a:
            if len(i) > 1 and not i.isalpha():
                tmp2 = []
                tmp2.append(list(i))
                tmp2 = [i for j in tmp2 for i in j]
                for j in tmp2:
                    tmp.append(j)
            else:
                tmp.append(i)
        a = tmp
        tmp = []
        # (sorted([i for i in a], key=len, reverse=True))
        # print(a)   
        return set(a) 