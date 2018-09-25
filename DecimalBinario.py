n = 51387656
a = n
r = 0
z = []



while (n > 0):
    r = n % 2
    n = int(n/2)
    z.insert(0, r)

def convertirDecimalABinario(numeroAConvertir, residuo, lista):
    if (numeroAConvertir <= 0):
        return lista
    else:
        residuo = numeroAConvertir % 2
        w = (int(numeroAConvertir / 2))
        lista.insert(0, residuo)
        return convertirDecimalABinario(w, residuo, lista)

resultado = []
resultado2 = []
numeroAConvertir = 2

resultado = convertirDecimalABinario(numeroAConvertir, 0, resultado2)

print ('numero: ',numeroAConvertir)
print (resultado)