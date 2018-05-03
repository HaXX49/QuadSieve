import libPrime as prime
import libQuadSieve as QS
from math import gcd as pgcd

def addlist(l1,l2):
    res = []
    if len(l1)==len(l2):
        for k in range(len(l1)) :
            res.append(l1[k]+l2[k])
    return res

ex = QS.support_friable(21311,60,13)
# print('1) Support Friable:',ex)
tst = dict()
for key in ex.keys() :
    tst[key] = prime.ifactor(ex[key])
# print('2) Création d\'un dictionnaire de décompositions :',tst)

#On constitue la liste des facteurs utilisés lors des différentes décompositions
fact = set()
for dec in tst.values():
    fact.update(dec)
fact_list = list(fact)
fact_list.sort()
# print(fact_list)

#On établit la matrice des puissances des différents facteurs
ex2 = dict()
for key in tst.keys():
    for dec in tst.values():
        ex2[key] = list()
        # print(tst[key])
        for k in fact_list :
            ex2[key].append(tst[key].count(k))

#On crée la matrice de parité des puissances
ex3 = dict()
for key in ex2.keys():
    ex3[key] = list()
    for k in ex2[key]:
        ex3[key].append(k%2)
# print(ex3)

# for k in ex3.keys():
#     print(f'{k} | {ex3[k]}')


matrice_parite = ex3
def qs_parcours(dico,m,n):
    a = []
    #Recherche d'une ligne nulle
    # for key in dico.keys():
    #     if dico[key] == [0]*len(dico[key]):
    #         a.append(key)
    #Recherche combinaison linéaire paire
    for key1 in dico.keys():
        for key2 in dico.keys():
            #On enlève le cas où on est à la même ligne
            if key1!=key2:
                if (sum(dico[key1])+sum(dico[key2]))%2 == 0:
                    a.append(key1,key2)
                    return a

def qs_facteurs(a,m,n): 
    #Calcul des co-facteurs
    #Cas ou len(a) = 1
    if len(a)==1:
        x1 = pgcd(m+a[0]-int(QS.P(a[0],n)**0.5),n)
        x2 = pgcd(m+a[0]+int(QS.P(a[0],n)**0.5),n)
    #Cas où len(a) = 2
    if len(a)==2:
        x1 = pgcd((m+a[0])*(m+a[1])+int((QS.P(a[0],n)*QS.P(a[1],n))**0.5),n)
        x2 = pgcd((m+a[0])*(m+a[1])-int((QS.P(a[0],n)*QS.P(a[1],n))**0.5),n)
    # if prime.isPrime(x1) and prime.isPrime(x2):
    #     print('x1 et x2 premiers')
    return(x1,x2)

def quadsieve(dico,m,n):
    return qs_facteurs(qs_parcours(dico,m,n),m,n)

print(quadsieve(matrice_parite,146,21311))