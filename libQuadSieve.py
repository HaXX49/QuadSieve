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
            
print(Legendre(3,29))
print(Legendre(3,29) == -1)
print(Legendre(111,41))
print(Legendre(111,41)==-1)
print(Legendre(113,41))
print(Legendre(113,41)==1)
    
