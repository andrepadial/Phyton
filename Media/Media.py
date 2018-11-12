qtdTotal = int(input('Informe a quantidade de alunos: '))
contProvas = int(input('Informe a quantidade de notas: '))

contAluno = 1
contNotas = 1
aux = 0
media = 0
mediaGeral = 0


while contAluno <= qtdTotal:
    nome = input('Informe o nome do aluno ' + str(contAluno) + ' : ')
    
    while contNotas <= contProvas:
        aux = float(input('Informe a nota ' + str(contNotas) + ' do aluno ' + nome + ': '))
        media += aux
        contNotas += 1
    
    media = media / contProvas
    mediaGeral += media
    
    contNotas = 1
    print("Aluno: " + nome + " média - " + str(round(media, 2)))
    aux = 0
    media = 0
    contAluno += 1

contAluno = 1
mediaGeral = mediaGeral / qtdTotal

print("Media geral dos alunos - " + str(round(mediaGeral, 2)))

    