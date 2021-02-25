# Desafio nº 6 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n = int(input('Insira um número: '))
nd = n*2
nt = n*3
nr = n ** (1/3)
print('O dobro de {} é {}.'.format(n, nd))
print('O triplo de {} é {}.'.format(n, nt))
print('A raiz quadrada de {} é {}.'.format(n, nr))
