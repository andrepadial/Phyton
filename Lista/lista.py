listaItems = list()
qtd = int(input('Informe a quantidade de elementos: '))

def populaLista(qtd):
    
    lista = list()
    contador = 0
    
    while(contador <= qtd - 1):
        numero = str(input('Informe o ' + str(contador + 1) + 'o elemento: '))
        lista.append(str(numero))
        
        contador += 1
        
    return lista

listaItems = populaLista(qtd)
print(listaItems)


item1 = listaItems[0]
listaItems.remove(str(item1))
print(listaItems)

incluirNovoItem = str(input('Informe o novo valor: '))
listaItems.append(incluirNovoItem)
print(listaItems)

listaItems.sort()
print(listaItems)

cont = len(listaItems)
listaItems.pop(cont - 1)
print(listaItems)

listaItems.reverse()
print(listaItems)

