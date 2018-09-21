author = 'Leonel Gonzalez Vidales'
numeros = [6, 8, 9, 12, 23, 19, 65, 33, 78, 89, 26, 45, 31]
#print (numeros)



c = 0
for i in range(int(len(numeros) / 2)):
    c = c - 1
    x = numeros[i]
    numeros[i] = numeros[c]
    numeros[c] = x
#print (numeros)

longitud = int(len(numeros)) - 1
a = int(0)

while((longitud - a) >= a):
    aux = numeros[a]
    numeros[a] = numeros[longitud - a]
    numeros[longitud - a] = aux
    a = a + 1
#print (numeros)

while(a <= (longitud - a)):
    aux = numeros[a]
    numeros[a] = numeros[longitud - a]
    numeros[longitud - a] = aux
    a = a + 1

# [6, 8, 9, 12, 23, 19, 65, 33, 78, 89, 26, 45, 31]
# [0, 1, 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
# [i                                             f] x
# [   i                                     f     ]
# [      i                              f         ]
# [          i                       f            ]
# [              i               f                ]
# [                  i       f                    ]
# [                      if                       ]

# [i                                             f]
# [6                                            31]
# aux = 31
# [6                                             6]
# [31                                            6]


def invertirArreglo(lista, i, f):
    while(i <= f):
        # i = 0, f = 12
        print (lista)
        print (i, f)
        aux = lista[f]
        lista[f] = lista[i]
        lista[i] = aux
        return invertirArreglo(lista, i + 1, f - 1)
    return lista

list = [5, 500, 10, 7, 5, 20, -4, 19, 10, 3, 2, 56]
#print (list)
f = int(len(list)) - 1
lista_invertida = invertirArreglo(list, 0, f)
print (lista_invertida)



