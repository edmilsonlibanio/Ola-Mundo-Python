# Desafio nº 7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média (atenção ao resultado ordem de precedência).

aluno = input('Insira o nome do aluno: ')
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
soma = nota1 + nota2
media = soma/2
print('A nota média de {} foi: {} '.format(aluno, media))
