import libPrime as prime
import libQuadSieve as QS

def P(x,N):
    M = int(N**0.5)
    return (x+M)**2-N

def database_M(C,N):
    M = int(N**0.5)
    dico = dict()
    for x in range(0,C):
        dico[x+M]=prime.ifactor(P(x,N))
    return dico

base = prime.liste_prime(50)
print(prime.base_factor(7429,base))

# liste = list()
# for C in range(0,30):
#     # print(P(C,7429))
#     # print(prime.base_factor(P(C,7429),base))
#     print(f'P({C}) = {C+86}^2 = {P(C,7429)} = {prime.ifactor(P(C,7429))}')
# print(liste)