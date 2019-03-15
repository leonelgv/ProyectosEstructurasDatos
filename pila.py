__author__ = 'Leonel Gonzalez Vidales'

class Pila:
    def __init__(self):
        self.items=[]

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == []

    def tamanio(self):
        return len(self.items)

    def cima_pila(self):
        return self.items[-1]

