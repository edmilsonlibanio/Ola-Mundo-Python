# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Informe um número qualquer: '))
if numero == 0 or numero % 2 == 0:
    print(f'O número {numero} digitado é par.')
else:
    print(f'O número {numero} digitado é impar.')
