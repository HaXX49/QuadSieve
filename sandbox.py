import libPrime as prime

def P(x,N):
    M = int(N**0.5)
    return (x+M)**2-N

for C in range(-10,10):
    # print(P(C,7429))
    print(prime.ifactor(P(C,7429)))