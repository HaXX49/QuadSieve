def liste_prime(n):
    '''Retourne les n premiers nombres premiers'''
    result = list()
    k=1
    while len(result) < n:
        k +=1
        if len(ifactor(k)) == 1:
            result.append(k)
    return result

def ifactor(n, simple = True,f=[]):
    '''Retourne la liste des facteurs de n'''
    f = []  # facteurs premiers de n (répétitions possibles)
    p = 2  # diviseur premier de n
    if n<0 :
        f.append(-1) 
        n = -1*n
    while p * p <= n:  # pareil que p <=sqrt(n)
        if n % p == 0:
            f += [p]
            n //= p
        else:
            p = 3 if p == 2 else p + 2
    f += [n]
    if simple :
        return f
    else:
        return sorted([(p, f.count(p)) for p in set(f)], key=lambda x: x[0])
    
def isPrime(x):
        return 1 == len(ifactor(x))

def base_factor(n, base, rep=[]):
    if n==1:
        # return rep
        return sorted([(p, rep.count(p)) for p in set(rep)], key=lambda x: x[0])
    if n<0:
        rep.append(-1)
        return base_factor(-1*n,base,rep)
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