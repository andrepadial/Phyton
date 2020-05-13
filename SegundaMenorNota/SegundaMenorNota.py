from statistics import mean, median, mode, stdev

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        

def populaLista(qtd):
    lista = list()
    contador = 0
    
    while(contador <= qtd - 1):
        nome = str(input('Informe o nome do ' + str(contador + 1) + 'o aluno: '))
        nota = float(input('Informe a nota do ' + str(contador + 1) + 'o aluno: '))
        
        lista.append(Aluno(nome, nota))
        contador += 1
        
    return lista
    
    
    
def imprimeAlunos(lista):
    for al in lista:
        print(al.nome + ' - ' + str(al.nota))
        
        

def removeMenorNota(lista):
    al = min(lista, key=lambda x: x.nota)
    listaAux = list()
    listaAux = filter(lambda x: x.nota != al.nota, lista)
    
    return listaAux
    
    
    
def getMenor2aNota(lista):
    
    menor2 = min(lista, key=lambda z: z.nota)
    listaAux = list()
    listaAux = filter(lambda m2: m2.nota == menor2.nota, listAluno)
    return listaAux
    

def imprimeDados(lista):
    
    print('Soma: ' + str(sum(aluno.nota for aluno in lista)))
    print('Média: ' + str((sum(aluno.nota for aluno in lista) / len(lista))))
    
    data_points = [float(aluno.nota) for aluno in lista]
    mode([x for x in data_points])
    

listAluno = list()
qtd = int(input('Informe a quantidade de alunos: '))
listAluno = populaLista(qtd)
print('Alunos e notas:')
imprimeAlunos(listAluno)
print('Alunos com a 2a menor nota:')
imprimeAlunos(getMenor2aNota(removeMenorNota(listAluno)))
print('Estatísticas ')
imprimeDados(listAluno)

