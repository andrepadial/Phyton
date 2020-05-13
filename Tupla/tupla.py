listaItems = list()
qtd = int(input('Informe a quantidade de elementos: '))

def populaLista(qtd):
    
    lista = list()
    contador = 0
    
    while(contador <= qtd - 1):
        numero = str(input('Informe o ' + str(contador + 1) + 'o número: '))
        lista.append(hash(numero))
        contador += 1
        
    return lista


print(tuple(populaLista(qtd)))