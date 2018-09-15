author = 'Leonel Gonzalez Vidales'
numeros = [6, 8, 9, 12, 23, 19, 65, 33, 78, 89, 26, 45, 31]
print (numeros)
c = 0
for i in range(int(len(numeros) / 2)):
    c = c - 1
    x = numeros[i]
    numeros[i] = numeros[c]
    numeros[c] = x
print (numeros)


longitud = int(len(numeros)) - 1
a = int(0)

while((longitud - a) > a):
    aux = numeros[a]
    numeros[a] = numeros[longitud - a]
    numeros[longitud - a] = aux
    a = a + 1

print (numeros)

#print (numeros[::-1])

#print (reverse("lista"))
# list[start:end]
# list[start:]
# list[:end]
# list[:]
# list[start:end:step]

print (numeros[:-3:-1])