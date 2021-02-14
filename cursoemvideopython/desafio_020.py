from random import shuffle
aluno_01 = str(input('Informe o nome do aluno: '))
aluno_02 = str(input('Informe o nome do aluno: '))
aluno_03 = str(input('Informe o nome do aluno: '))
aluno_04 = str(input('Informe o nome do aluno: '))
lista = [aluno_01, aluno_02, aluno_03, aluno_04]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será:')
print(lista)
 