listaItems = list()
qtd = int(input('Informe a quantidade de elementos: '))

def populaLista(qtd):
    
    lista = list()
    contador = 0
    
    while(contador <= qtd - 1):
        numero = int(input('Informe o ' + str(contador + 1) + 'o elemento: '))
        lista.append(numero)
        
        contador += 1
        
    return lista
    

def retornaMaior2(lista):
    
    maior = max(listaItems)
    maior2 = 0
    contador = 1
    
    if (max(listaItems)) in lista:
        lista.remove(max(listaItems))
        
    for val in lista:
        if (contador == 1):
            maior2 = val
        else:
            if (val > maior2):
                maior2 = val
        
        contador += 1
    
    return maior2


listaItems = populaLista(qtd)
print(listaItems)

print(str(retornaMaior2(listaItems)))

