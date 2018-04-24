def Legendre(m, n):
    '''Renvoie le symbole de Legendre de m et n'''
    if m>m%n :
        return Legendre(m%n, n)
    #Cas particuliers
    if m == 0:
        return 0
    if m == 1:
        return 1
    #réduction par modulo
    if n%2 == 1:
        if m%2 == 0:
            if (n%8 == 1) or (n%8 == 7):
                return Legendre(m//2, n)
            if (n%8 == 3) or (n%8 == 5):
                return (-1)*Legendre(m//2, n)
        if m%2 == 1:
            if (n%4 == m%4) and (n%4 == 3):
                return (-1)*Legendre(n, m)
            else :
                return Legendre(n, m)

def base_reg(p, n):
    '''Retourne une base régulière selon p de taille n'''
    base = [-1]
    k=1
    while len(base) < n:
        k +=1
        if ((len(prime.ifactor(k)) == 1) and (QS.Legendre(k,p) == 1)):
            base.append(k)
    return base



