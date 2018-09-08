__author__ = 'Leonel Gonzalez'

from esfera import *
from memoria_estatica import *
Esferita = Esfera(56)
"""
print "El radio es:" , Esferita.getRadio()
print "El diametro es:" , Esferita.getDiametro()
print "La circunferencia es: ", Esferita.getCircunferencia()
print "El area es: ", Esferita.getArea()
print "El volumen es: ", Esferita.getVolumen()
arreglo = memoria_estatica()
arreglo.recorrerArreglo()
print 'Agregar elemento'
elemento = raw_input()
arreglo.agregarelementoarray(elemento)
arreglo.recorrerArreglo()

"""
promedio = 9.67
otralista = []
supermercado = ['fruta','agua', 'refresco', 'pan', 'pastel']
estructuradedatos = ['agustin pimentel', 'francisco pineda', 'enrique bello']
precios = [12, 34, 45, 47]
porcentajes = [.34, .56, .12, 1.2]

print ('Primera lista')
print (supermercado)
supermercado.append('jamon')

print ('Uso de append')
print (supermercado)


print ('Uso de copy')
otralista = supermercado.copy()
print (otralista)

otralista.clear()
otralista.append('pera')
otralista.append('manzana')
print (otralista)
supermercado.extend(otralista)
print (supermercado)
supermercado.append('agua')
print (supermercado)
print ('la lista supermercado tiene ', supermercado.count('agua'))
supermercado.insert(0, 'galletas')
print (supermercado)
supermercado.pop(2)
print (supermercado)
supermercado.remove('pera')
print (supermercado)
supermercado.sort()
print(supermercado)
supermercado.reverse()
print(supermercado)