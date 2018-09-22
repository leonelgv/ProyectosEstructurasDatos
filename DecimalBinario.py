n = 51387656
a = n
r = 0
z = []



while (n > 0):
    r = n % 2
    n = int(n/2)
    z.insert(0, r)

def convertirDecimalABinario(w, residuo, lista):
    print (w)
    if (w <= 0):
        return lista
    else:
        print(w)
        residuo = w % 2
        w = (int(w / 2))
        lista.insert(0, residuo)
        return convertirDecimalABinario(w, 0, lista)

resultado = []
resultado2 = []
numeroAConvertir = 4999

resultado = convertirDecimalABinario(numeroAConvertir, 0, resultado2)

print ('numero: ',numeroAConvertir)
print (resultado)