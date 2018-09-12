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

listas = memDinamica(supermercado)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('cerveza')
listas.imprimirLista()

lista2 = memDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(89)
lista2.imprimirLista()
