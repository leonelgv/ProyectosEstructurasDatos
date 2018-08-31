__author__ = 'Leonel Gonzalez'

from esfera import *
from memoria_estatica import *
Esferita = Esfera(56)
elemento = ''
"""
print "El radio es:" , Esferita.getRadio()
print "El diametro es:" , Esferita.getDiametro()
print "La circunferencia es: ", Esferita.getCircunferencia()
print "El area es: ", Esferita.getArea()
print "El volumen es: ", Esferita.getVolumen()
"""

arreglo = memoria_estatica()
arreglo.recorrerArreglo()
print 'Agregar elemento'
elemento = raw_input()
arreglo.agregarelementoarray(elemento)
arreglo.recorrerArreglo()

