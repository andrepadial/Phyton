valor = int(input('Informa um valor: '))

if (valor % 2 == 0):
    if(valor >= 2 and valor <= 5):
        print('Not Weird')
    elif(valor >= 6 and valor <= 20):
        print('Weird')
    else:
        print('Not Weird')
else:
    print('Not Weird')