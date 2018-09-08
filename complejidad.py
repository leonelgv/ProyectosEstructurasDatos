"""
Algoritmo para realizar la suma aritmetica del 1 al n
"""

"""
Aqui puedes cambiar el valor de n
"""
n = 1000000
suma = 0;
suma2 = 0;


"""
Algoritmo 1. Se utiliza la formula (n * (n + 1))/2 para realizar la suma
"""

suma = (n * (n + 1)) / 2

print 'La suma es', suma

"""
Algoritmo 2. Se utiliza un ciclo for para realizar la suma 
"""
for x in range(1, n + 1):
    suma2 += x

print 'La suma es', suma2


