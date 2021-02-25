# Desafio nº 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno_01 = input('Informe o nome do aluno: ')
aluno_02 = input('Informe o nome do aluno: ')
aluno_03 = input('Informe o nome do aluno: ')
aluno_04 = input('Informe o nome do aluno: ')

lista = [aluno_01, aluno_02, aluno_03, aluno_04]

escolhido = random.choice(lista)

print('Prezado Professor, a sua turma de matemática é formada pelos alunos: {}, {}, {} e {}.'.format( aluno_01, aluno_02, aluno_03, aluno_04))

print('O aluno {} apagará o quadro hoje!'.format(escolhido))





# Nesse exercício aprendemos a importação do módulo Random na linha 2. Outro conceito aprendido foi o de lista na linha 9, onde #lista é uma variavel que tem como parametros os seus itens listados e separados por virgula dentro de chaves [a, b,c, d].

# Na linha 11 vemos a aplicação do método # choice dentro do módulo random. 

# Outra uma vez que o método choice foi o responsável por escolher um item dentro da lista, uma segunda forma de resolver o exercício é importar apenas o método choice dentro do módulo random, conforme abaixo: (e claro, apagar o nome o # random do código)

#from random import choice
#a1 = input('Nome do Aluno: ')
#a2 = input('Nome do Aluno: ')
#a3 = input('Nome do Aluno: ')
#a4 = input('Nome do Aluno: ')
#lista = [a1, a2, a3, a4]
#escolhido = choice(lista)
#print('O aluno {} apagará o quadro hoje!'.format(escolhido))
