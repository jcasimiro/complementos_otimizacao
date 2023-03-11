def Fibonnaci(n):
    if ( n==0):
        return 0
    if ( n == 1):
        return 1
    return Fibonnaci(n-1) + Fibonnaci(n-2)

def Fibonnaci_linear(n):
    if ( n==0):
        return 0
    if ( n == 1):
        return 1

print(Fibonnaci(10))
print(Fibonnaci(36))
print(Fibonnaci(38))