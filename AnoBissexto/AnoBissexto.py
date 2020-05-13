ano = int(input('Informe o ano: '))
validacao = False

def validacaoBissexto(anoBissexto):
    
    if(anoBissexto % 4 == 0):
        if(anoBissexto % 400 == 0):
            validacao = True
        elif(anoBissexto % 100 == 0):
            validacao = False
    else:
        validacao = False
        
    return validacao
    

print(validacaoBissexto(ano))
