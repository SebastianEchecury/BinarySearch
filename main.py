import random, time

def naiveSearch(lista, objeto): # Busqueda secuencial
    for x in range(len(lista) - 1):
        if lista[x] == objeto:
            return x
    return -1 # Si no encuentra el objeto devuelvo -1

def binarySearch(lista, objeto, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lista) - 1

    if high < low:
        return -1

    midPoint = (low + high) // 2
    if lista[midPoint] == objeto:
        return midPoint
    elif objeto < lista[midPoint]:
        return binarySearch(lista, objeto, low, midPoint-1)
    else:
        return binarySearch(lista, objeto, midPoint+1, high)


lista = list()
for x in range(60000000):
    lista.append(x)

objetivo = random.choice(lista)

print('Numero a encontrar: ' + str(objetivo))


inicioNS = time.time()
print(naiveSearch(lista, objetivo))
finNS = time.time()
print('Naive Search time: ', (finNS - inicioNS), ' segundos')

inicioBS = time.time()
print(binarySearch(lista, objetivo))
finBS = time.time()
print('Binary Search time: ', (finBS - inicioBS), ' segundos')