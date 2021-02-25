# Desafio nº 5 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Insira um número: '))
print('O número {} é precedido pelo número {} e sucedido pelo número {}.'.format(n, (n-1), (n+1)))
