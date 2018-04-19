def liste_prime(n):
    '''Retourne les n premiers nombres premiers'''
    result = list()
    k=1
    while len(result) < n:
        k +=1
        if len(ifactor(k)) == 1:
            result.append(k)
    return result

def ifactor(n):
    '''Retourne la liste des facteurs de n'''
    f = []  # facteurs premiers de n (répétitions possibles)
    p = 2  # diviseur premier de n
    while p * p <= n:  # pareil que p <=sqrt(n)
        if n % p == 0:
            f += [p]
            n //= p
        else:
            p = 3 if p == 2 else p + 2
    f += [n]
    #return sorted([(p, f.count(p)) for p in set(f)], key=lambda x: x[0])
    return f

def base_factor(n, base, rep=list()):
    if n==1:
        return rep
    for k in base:
        if n%k==0:
            rep.append(k)
            return base_factor(n//k, base, rep)

def nmb_puiss(liste):
    liste_puiss = list()
    for k in set(liste):
        liste_puiss.append(liste.count(k))
    return liste_puiss


def nb_divis(n):
    resultat = 1
    liste = nmb_puiss(ifactor(n))
    for k in liste:
        resultat *= k+1
    return resultat

def isParfait(n):
    '''Détecte si un nombre est un carré parfait'''
    return nb_divis(n)%2==1

def isInt(f):
    return f == int(f)