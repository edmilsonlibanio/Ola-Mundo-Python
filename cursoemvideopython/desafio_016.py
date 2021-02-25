# Desafio nº 16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Dica: Olhar todas as funções que tem dentro do módulo math usado na aula.

from math import trunc
numero = float(input('Insira um número real: '))
inteira = trunc(numero)
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(numero, inteira))

# no exercicio acima eu importei apenas a função truncate e não a biblioteca toda de Python. Por conta disso na linha 3 eu coloquei inteira = trunc(numero)

# existe a opção de responder este mesmo exercício importando toda a biblioteca de matemática, conforme abaixo:

import math
numero = float(input('Insira um número real: '))
inteira = math.trunc(numero)
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(numero, inteira))

# Uma terceira forma de resolver este problema é fazê-lo sem precisar importar a biblioteca de matemática. Usando a função interna do Python int (inteiro), conforme abaixo:

numero = float(input('Insira um número real: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format( numero, int(numero)))
