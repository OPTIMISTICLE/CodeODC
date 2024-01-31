n = input("entrer un nombre entre 0 et 1000 ")
n = int(n)
while n > 1000:
    n = input("entrer un nombre entre 0 et 1000")

def computeMultiplesSum(n):
    """Cette fonction renvoie la somme de tous les mutliples positifs de 3 ou 5 ou 7 strictement inferieur a n"""

    x = 3
    y = 5
    z = 7
    summ = 0
    for i in range(n):
        if x * i < n:
            summ += x * i
        if y * i < n:
            summ += y * i
        if z * i < n:
            summ += z * i
        
    return summ

print(computeMultiplesSum(n))