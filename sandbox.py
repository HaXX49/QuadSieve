from libPrime import liste_prime
def base_factor(n, base, rep=list()):
    if n==1:
        return rep
    for k in base:
        if n%k==0:
            rep.append(k)
            return base_factor(n//k, base, rep)

base = liste_prime(20)
print(base_factor(126,base))